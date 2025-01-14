from talon import Context, actions, settings

ctx = Context()

ctx.matches = r"""
code.language: julia
"""

ctx.lists["user.code_common_function"] = {
	# base julia
	"correlation": "cor",
	"covariance": "cov",
	"eigen": "eigen",
	"get working directory": "pwd",
	"head": "head",
	"length": "length",
	"log": "log",
	"make directory": "mkdir",
	"max": "max",
	"mean": "mean",
	"min": "min",
	"print": "print",
	"run": "run",
	"sort": "sort",
	"sortperm": "sortperm",
	"sum": "sum",
	"tail": "tail",
	"trim white space": "trimws",
	"type": "typeof",
	"unique": "unique",
	"view": "@view",
}

ctx.lists["user.code_libraries"] = {
    "arg parse": "ArgParse",
    "bezier": "Bezier",
	"Cairo Makie": "CairoMakie",
    "CIFTI": "CIFTI",
    "chain": "Chain",
    "clustering": "Clustering",
    "colors": "Colors",
    "CorticalParcels": "CorticalParcels",
    "CorticalSurfaces": "CorticalSurfaces",
    "cSV": "CSV",
    "dataFrames": "DataFrames",
    "dates": "Dates",
    "distributions": "Distributions",
    "geometry basics": "GeometryBasics",
	"GL Makie": "GLMakie",
    "graphs": "Graphs",
    "HDF 5": "HDF5",
    "interpolations": "Interpolations",
    "JLD": "JLD",
    "JSON": "JSON",
    "linear algebra": "LinearAlgebra",
    "match": "Match",
    "named arrays": "NamedArrays",
    "nifti": "NIfTI",
    "open CV": "OpenCV",
    "ordered collections": "OrderedCollections",
    "package compiler": "PackageCompiler",
    "PKG templates": "PkgTemplates",
    "python call": "PythonCall",
    "sockets": "Sockets",
    "SQ light": "SQLite",
    "statistics": "Statistics",
	"stats base": "StatsBase",
    "word frequency distributions": "WordFrequencyDistributions",
}

ctx.lists["user.code_parameter_name"] = {
	"alpha": "alpha",
	"breaks": "breaks",
	"colour": "colour",
	"data": "data",
	"fill": "fill",
	"H just": "hjust",
	"keep": ".keep",
	"label": "label",
	"labels": "labels",
	"log": "log",
	"main": "main",
	"mapping": "mapping",
	"method": "method",
	"NA remove": "na.rm",
	"path": "path",
	"position": "position",
	"plex label": "xlab",
	"plex limit": "xlim",
	"scales": "scales",
	"size": "size",
	"show legend": "show.legend",
	"sort": "sort",
	"title": "title",
	"type": "type",
	"vee just": "vjust",
	"width": "width",
	"with ties": "with_ties",
	"why label": "ylab",
	"why limit": "ylim",
	"why max": "ymax",
	"why min": "ymin",
}


@ctx.action_class("user")
class UserActions:
	def code_operator_assignment():
		actions.auto_insert(" = ")

	def code_operator_subtraction():
		actions.auto_insert(" - ")

	def code_operator_addition():
		actions.auto_insert(" + ")

	def code_operator_multiplication():
		actions.auto_insert(" * ")

	def code_operator_exponent():
		actions.auto_insert(" ^ ")

	def code_operator_division():
		actions.auto_insert(" / ")

	def code_operator_modulo():
		actions.auto_insert(" % ")

	def code_operator_equal():
		actions.auto_insert(" == ")

	def code_operator_not_equal():
		actions.auto_insert(" != ")

	def code_operator_greater_than():
		actions.auto_insert(" > ")

	def code_operator_greater_than_or_equal_to():
		actions.auto_insert(" >= ")

	def code_operator_less_than():
		actions.auto_insert(" < ")

	def code_operator_less_than_or_equal_to():
		actions.auto_insert(" <= ")

	def code_operator_and():
		actions.auto_insert(" && ")

	def code_operator_or():
		actions.auto_insert(" || ")

	def code_operator_bitwise_and():
		actions.auto_insert(" & ")

	def code_insert_null():
		actions.auto_insert("nothing")

	def code_state_if():
		actions.insert("if end")
		actions.key("left:3 enter up end")

	def code_state_else_if():
		actions.insert("else if ")

	def code_state_else():
		actions.key("backspace")
		actions.insert("else")
		actions.key("enter")

	def code_state_for():
		actions.insert("for end")
		actions.key("left:3 enter up end")

	def code_state_while():
		actions.insert("while end")
		actions.key("left:3 enter up end")

	def code_import():
		actions.auto_insert("using ")

	def code_comment_line_prefix():
		actions.auto_insert("#")

	def code_state_return():
		actions.auto_insert("return ")

	def code_break():
		actions.auto_insert("break")

	def code_next():
		actions.auto_insert("continue")

	def code_insert_true():
		actions.auto_insert("true")

	def code_insert_false():
		actions.auto_insert("false")

	def code_insert_function(text: str, selection: str):
		text += f"({selection or ''})"
		actions.user.paste(text)
		actions.edit.left()

	def code_private_function(text: str):
		result = "function {}() \n\nend".format(
			actions.user.formatted_text(
				text, settings.get("user.code_private_function_formatter")
			)
		)

		actions.user.paste(result)
		actions.edit.up()
		actions.edit.up()
		actions.edit.line_end()
		actions.edit.left()
		actions.edit.left()

	def code_insert_library(text: str, selection: str):
		actions.auto_insert("using ")
		actions.user.paste(text + selection)

	def code_insert_named_argument(parameter_name: str):
		actions.insert(f"{parameter_name} = ")
