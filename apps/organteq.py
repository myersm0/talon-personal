import subprocess
import json
from talon import Module

mod = Module()

@mod.action_class
class Actions:
	def toggle_organteq_stop(manual: str, stop: int):
		"""toggle an Organteq stop on or off"""
		endpoint = "http://127.0.0.1:8081/jsonrpc"
		parameter_id = f"Stop[{manual}][{stop}].Switch"
		
		get_payload = {
			"method": "getParameters",
			"params": [{"id": parameter_id}],
			"jsonrpc": "2.0",
			"id": 1
		}
		
		try:
			result = subprocess.run(
				f'curl -X POST {endpoint} -H "Content-Type: application/json" -d \'{json.dumps(get_payload)}\'',
				shell=True,
				check=True,
				capture_output=True,
				text=True
			)
			
			response = json.loads(result.stdout)
			current_value = response["result"][0]["normalized_value"]
			new_value = 0.0 if current_value == 1.0 else 1.0
			
			set_payload = {
				"method": "setParameters",
				"params": [{"id": parameter_id, "normalized_value": new_value}],
				"jsonrpc": "2.0",
				"id": 2
			}
			
			subprocess.run(
				f'curl -X POST {endpoint} -H "Content-Type: application/json" -d \'{json.dumps(set_payload)}\'',
				shell=True,
				check=True
			)
			
		except (subprocess.CalledProcessError, json.JSONDecodeError, KeyError) as e:
			print(f"Command failed with error: {e}")

