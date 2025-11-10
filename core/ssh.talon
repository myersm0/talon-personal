app: /term/i
-

^tim's server$:
	ssh michael.myers@myelin1.wustl.edu

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







