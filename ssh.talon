app: /term/i
-

^chpc$:
	insert("ssh login3.chpc.wustl.edu -l michael.myers -X")

^chpc as service user$:
	insert("ssh -X nrg-svc-hcpi@10.27.136.152")

^shadow <number>$:
	insert("ssh hcpi-shadow")
	insert(number)
	insert(".nrg.wustl.edu -l michael.myers -X")

^shadow <number> as service user$:
	insert("ssh hcpi-shadow")
	insert(number)
	insert(".nrg.wustl.edu -l nrg-svc-hcpi -X")








