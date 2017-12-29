# -*- coding:utf-8 -*-
'''
xxxxxxxxx

'''
import random
import argparse
import xml.etree.cElementTree as ET

STARTED, RUNNING, STOPPED = range(3)

def stop_times(speed_list):
	cur_state = STARTED
	prev_state = STARTED
	stops = 0
	stop_time = 0
	for k, spd in enumerate(speed_list):
		if spd == 0:
			if prev_state == RUNNING:
				stops += 1
				stop_time += 1
				cur_state = STOPPED
			if prev_state == STOPPED:
				stop_time += 1
		elif prev_state == STOPPED:
			cur_state = RUNNING
		elif prev_state == STARTED:
			cur_state = RUNNING

		prev_state = cur_state

	return stop_time, stops

if __name__ == '__main__':
	random.seed(100)
	parser = argparse.ArgumentParser(description="calculate di contest loss.")
	parser.add_argument("--trip", default="")
	parser.add_argument("--netstat", default="")

	args = parser.parse_args()

	#calculate wait times
	trip_file = args.trip
	wait_steps = 0
	time_loss = 0
	net_trip = ET.ElementTree(file=trip_file)
	net_trip_root = net_trip.getroot()
	tripinfos = net_trip_root.findall('tripinfo')
	for tripinfo in tripinfos:
		per_wait_steps = tripinfo.attrib['waitSteps']
		wait_steps += int(per_wait_steps)
		per_time_loss = tripinfo.attrib['timeLoss']
		time_loss += float(per_time_loss)

	#calculate stop times of all vehicle
	vehicle_spd_dict = {}
	netstat_file = args.netstat
	net_stats = ET.ElementTree(file=netstat_file)
	net_trip_root = net_stats.getroot()
	timesteps = net_trip_root.findall('timestep')
	for timestep in timesteps:
		edges = timestep.findall('edge')
		for edge in edges:
			lanes = edge.findall('lane')
			for lane in lanes:
				vehicles = lane.findall('vehicle')
				for vehicle in vehicles:
					veh_id = vehicle.attrib['id']
					spd = vehicle.attrib['speed']
					if veh_id in vehicle_spd_dict.keys():
						vehicle_spd_dict[veh_id].append(float(spd))
					else:
						vehicle_spd_dict[veh_id] = []
						vehicle_spd_dict[veh_id].append(float(spd))

	total_stops = 0
	total_stop_time = 0
	for veh_id in vehicle_spd_dict.keys():
		spds = vehicle_spd_dict[veh_id]
		stop_time, stops = stop_times(spds)
		total_stops += stops
		total_stop_time += stop_time

	di_score_invese = (time_loss + 100*total_stops)/len(vehicle_spd_dict.keys())

	print("time loss: " + str(time_loss) + ", wait steps: " + str(wait_steps) + ", stop time: " + str(total_stop_time) + ", stops: " + str(total_stops) + ", vehicles: " + str(len(vehicle_spd_dict.keys())) \
			+ ", di_score_inverse: " + str(di_score_invese) + ", di_score: " + str(1000.0/di_score_invese) \
	)

	# store results(fitness) to file
	fn_res = open("res.txt", 'w')
	fn_res.write(str(di_score_invese))
	fn_res.close()
