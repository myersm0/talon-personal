app: /term*/i

-

julia run tests:
	insert("julia --project=. test/runtests.jl")
	key(enter)

julia project:
	insert("julia --project=. test/runtests.jl")
	key(enter)

julia run pipeline:
	insert("/opt/julia-1.12.5/bin/julia --project=. bin/run_pipeline.jl data/source data/output --store /tmp/deep-littre-no-adjudication")
	key(enter)
