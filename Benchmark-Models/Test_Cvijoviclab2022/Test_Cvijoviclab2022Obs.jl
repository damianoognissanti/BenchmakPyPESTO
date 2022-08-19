function Test_Cvijoviclab2022(u, t, dynPar, obsPar, paramData, obsData, observableId, simulationId) 

	sebastian, damiano= u 
	alpha, beta, gamma, delta = dynPar 

	if observableId == "sebastian_measurement" 
		return sebastian 
	end

	if observableId == "damiano_measurement" 
		return damiano 
	end

end

function Test_Cvijoviclab2022_t0!(u0Vec, paramVec) 

	beta, alpha, delta, gamma = paramVec 

	sebastian = 8.0 
	damiano = 4.0 

	u0Vec .= sebastian, damiano
end

function Test_Cvijoviclab2022_sd!(u, t, sdPar, dynPar, paramData, obsData, observableId, simulationId) 

	sebastian, damiano= u 
	alpha, beta, gamma, delta = dynPar 

	if observableId == "sebastian_measurement" 
		noiseParameter1_sebastian_measurement = getObsOrSdParam(sdPar, paramData, obsData, observableId, simulationId, t, getObsPar=false)
		return noiseParameter1_sebastian_measurement 
	end

	if observableId == "damiano_measurement" 
		noiseParameter1_damiano_measurement = getObsOrSdParam(sdPar, paramData, obsData, observableId, simulationId, t, getObsPar=false)
		return noiseParameter1_damiano_measurement 
	end

end