import subprocess
import json
from talon import Module

mod = Module()

organteq_endpoint = "http://127.0.0.1:8081/jsonrpc"
organteq_current_manual = 3

def organteq_call(payload):
	"""make a JSON-RPC call to Organteq"""
	try:
		result = subprocess.run(
			f'curl -X POST {organteq_endpoint} -H "Content-Type: application/json" -d \'{json.dumps(payload)}\'',
			shell=True,
			check=True,
			capture_output=True,
			text=True
		)
		return result.stdout
	except subprocess.CalledProcessError as e:
		print(f"Command failed with error: {e}")
		return None

@mod.action_class
class Actions:
	def organteq_toggle_stop(manual: str, stop: int):
		"""toggle an Organteq stop on or off"""
		parameter_id = f"Stop[{manual}][{stop}].Switch"
		get_payload = {
			"method": "getParameters",
			"params": [{"id": parameter_id}],
			"jsonrpc": "2.0",
			"id": 1
		}
		response_text = organteq_call(get_payload)
		if not response_text:
			return
		try:
			response = json.loads(response_text)
			current_value = response["result"][0]["normalized_value"]
			new_value = 0.0 if current_value == 1.0 else 1.0
			set_payload = {
				"method": "setParameters",
				"params": [{"id": parameter_id, "normalized_value": new_value}],
				"jsonrpc": "2.0",
				"id": 2
			}
			organteq_call(set_payload)
		except (json.JSONDecodeError, KeyError) as e:
			print(f"Command failed with error: {e}")
	
	def organteq_clear_manual(manual: str):
		"""set all stops on a manual to 0.0"""
		max_stops = 20 if manual == "3" else 10
		for stop in range(1, max_stops + 1):
			parameter_id = f"Stop[{manual}][{stop}].Switch"
			set_payload = {
				"method": "setParameters",
				"params": [{"id": parameter_id, "normalized_value": 0.0}],
				"jsonrpc": "2.0",
				"id": 1
			}
			organteq_call(set_payload)
	
	def organteq_set_manual(manual: str):
		"""set the current manual for subsequent commands"""
		global organteq_current_manual
		organteq_current_manual = manual
	
	def organteq_get_manual() -> str:
		"""get the current manual"""
		return organteq_current_manual



