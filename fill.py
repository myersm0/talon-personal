from talon import Module, Context

mod = Module()
mod.list("pathname", desc = "My commonly used paths")

ctx_default = Context()
ctx_default.lists["user.pathname"] = {
	"previous":				"-",
	"edmund":				"/Volumes/edmund/contents/",
	"electra":				"/Volumes/electra/contents/",
	"falstaff":				"/Volumes/falstaff/contents/",
	"guinevere":			"/Volumes/guinevere/contents/",
	"gesualdo":				"/Volumes/gesualdo/contents/",
	"contents":				"~/contents/",
	"resources":			"~/resources/",
	"downloads":			"~/Downloads/",
	"documents":			"~/Documents/",
	"pictures":			    "~/Pictures/",
	"resources":			"~/resources/",
	"Talon user":			"~/.talon/user/",
	"my Talon":				"~/.talon/user/m/",
	"Talon community":	    "~/.talon/user/community/",
	"stact intake":		    "/ceph/intradb/inbox/CCF_MANUAL_TRANSFERS/CCF_STACT_ITK/",
	"ADCP intake":		    "/ceph/intradb/archive/CCF_ADCPWI_ITK/arc001/",
	"ADCP processing":      "/ceph/intradb/archive/CCF_ADCPWI_PRC/arc001/",
	"ADCP staging":         "/ceph/intradb/archive/CinaB/CCF_ADCPWI_STG/bids/",
	"CBA intake":           "/ceph/intradb/archive/CCF_CBA_ITK/arc001/",
	"CBA processing":       "/ceph/intradb/archive/CCF_CBA_PRC/arc001/",
	"CBA staging":          "/ceph/intradb/archive/CCF_CBA_STG/arc001/",
	"supercomputer logs":   "/ceph/scratch/intradb/build/chpc/build/nrg-svc-hcpi/",
	"IntraDb logs":         "/ceph/intradb/logs/pipeline/",
	"CinaB":                "/ceph/intradb/archive/CinaB/",
}



