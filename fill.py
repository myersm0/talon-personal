from talon import Module, Context

mod = Module()
mod.list("pathname", desc = "commonly use paths")

ctx_default = Context()
ctx_default.lists["user.pathname"] = {
	"desdemona":			"/media/m/desdemona/contents/",
	"daphne":				"/media/m/daphne/contents/",
	"diomedes":				"/media/m/diomedes/contents/",
	"contents":				"/home/m/contents/",
	"Talon user":			"/home/m/.talon/user/",
	"my Talon":				"/home/m/.talon/user/m/",
	"Talon community":	"/home/m/.talon/user/community/",
	"stact intake":	"/ceph/intradb/inbox/CCF_MANUAL_TRANSFERS/CCF_STACT_ITK/",
	"ADCP intake":	"/ceph/intradb/archive/CCF_ADCPWI_ITK/arc001/",
	"ADCP processing":	"/ceph/intradb/archive/CCF_ADCPWI_PRC/arc001/",
	"ADCP staging":	"/ceph/intradb/archive/CinaB/CCF_ADCPWI_STG/bids/",
	"CBA intake":	"/ceph/intradb/archive/CCF_CBA_ITK/arc001/",
	"CBA processing":	"/ceph/intradb/archive/CCF_CBA_PRC/arc001/",
	"CBA staging":	"/ceph/intradb/archive/CCF_CBA_STG/arc001/",
	"supercomputer logs": "/ceph/scratch/intradb/build/chpc/build/nrg-svc-hcpi/",
	"IntraDb logs": "/data/intradb/logs/pipeline/",
}



