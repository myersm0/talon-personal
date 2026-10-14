app: /term/i

-

julia run tests [{user.dont_go}]:
	insert("julia --project=. test/runtests.jl")
	go = dont_go or "go"
	user.optional_enter(go)

julia project [{user.dont_go}]:
	insert("julia --project=.")
	go = dont_go or "go"
	user.optional_enter(go)

julia main [{user.dont_go}]:
	insert("julia --project=. main.jl")
	go = dont_go or "go"
	user.optional_enter(go)

julia run pipeline [{user.dont_go}]:
	insert("/opt/julia-1.12.5/bin/julia --project=. bin/run_pipeline.jl data/source data/output --store /tmp/deep-littre-no-adjudication")
	go = dont_go or "go"
	user.optional_enter(go)



