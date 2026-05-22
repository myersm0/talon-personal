app: /term*/i
tag: user.wustl

-

# work project names
CCF {user.project} {user.project_qualifier}:
	insert("CCF_")
	insert(project)
	insert("_")
	insert(project_qualifier)


## slurm
cue stat [{user.dont_go}]: 
	insert('squeue -u $USER -o "%.18i %.9P %.8j %.8u %.2t %.10M %.6D %R"')
	go = dont_go or "go"
	user.optional_enter(go)

cue stat HCP:
	insert('squeue -o "%.18i %.9P %.8j %.8u %.2t %.10M %.6D %R" | grep HCP')
	go = dont_go or "go"
	user.optional_enter(go)

cue stat ADCP:
	insert('squeue -o "%.18i %.9P %.8j %.8u %.2t %.10M %.6D %R" | grep ADCP')
	go = dont_go or "go"
	user.optional_enter(go)


## ssh

^chpc$:
	insert("ssh login3.chpc.wustl.edu -l michael.myers -X")
	key(enter)

^chpc as service user$:
	insert("ssh -X nrg-svc-hcpi@10.27.136.151")
	key(enter)

^shadow <number>$:
	insert("ssh hcpi-shadow")
	insert(number)
	insert(".nrg.wustl.edu -l michael.myers -X")
	key(enter)

^shadow <number> as service user$:
	insert("ssh hcpi-shadow")
	insert(number)
	insert(".nrg.wustl.edu -l nrg-svc-hcpi -X")
	key(enter)

^brain mappers$:
	insert("ssh brainmappers@brainmappers-desktop5.wustl.edu")
	key(enter)

