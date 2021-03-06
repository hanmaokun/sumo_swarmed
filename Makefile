include environment

all: MainSeq  MainLan 

clean:
	rm -f  MainLan MainSeq MainWan core.* *.o *% *~ *.out
	
MainSeq: MainSeq.o 
#	$(CXX) $(LDFLAGS) $^ $(LOADLIBES) $(CPPFLAGS)  -o $@    
	$(CXX) $(LDFLAGS) $^ $(LOADLIBES) $(CPPFLAGS)  -o $@

MainLan: MainLan.o
	 $(CXX) $(LDFLAGS) $^ $(LOADLIBES) $(CPPFLAGS) -o $@  

#MainWan: MainWan.o 
#	 $(CXX) $(LDFLAGS) $^ $(LOADLIBES) $(CPPFLAGS) -o $@  
LAN:
#	$(RUN)  -v  -p4pg pgfileLan MainLan
	$(RUN)  -v  -np 2 MainLan PSO.cfg tl2/2-intersections/2/tlLogic.tmp tl2/2-intersections/2/info.500.twoIntersections.txt tl2/2-intersections/2/tlLogic.500.best-solution.xml results.txt
#WAN:
#	$(RUN)  -v  -p4pg pgfileWan MainWan

SEQ:

	./MainSeq PSO.cfg tl2/2-intersections/2/tlLogic.tmp tl2/2-intersections/2/info.500.twoIntersections.txt tl2/2-intersections/2/tlLogic.500.best-solution.xml  results.txt

DIDI_:
	./MainSeq PSO_didi.cfg tl2/7-intersections/7/tlLogic.tmp tl2/7-intersections/7/info.6664.sevenIntersections.txt tl2/7-intersections/7/tlLogic.6664.best-solution.xml results_didi.txt

DIDI:
	./MainSeq PSO_didi.cfg tl2/7-intersections/7/tlLogic.withY.tmp tl2/7-intersections/7/info.6664.sevenIntersections.txt tl2/7-intersections/7/tlLogic.6664.best-solution.xml results_didi.txt
