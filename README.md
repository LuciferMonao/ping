This is a simple python project to check your ping to a server regularly and to put the collected ping data into nice graphs.
The main programm is ping.py which pings the server sz.de every 4.9 Seconds. Every 10.000 calls it also executes the save function of the save_data.py script, which moves all the current ping data of the last 10000 class to a folder named data/.
To show the graph of the last pings, use the function show of the python script show_graph. The function has the arguments:
	SIZE: The maximum amount of pings shown, if there are more, the the pings will be averaged to the amount of size.
	DIFFERENCE: The minimum difference of the average graph to the median graph for the average graph to show, to always show the average graph set difference to -100
	QUALITY: Quality of the graph, number from 1 (worst) to 95 (best).
If you have any questions, contact me via my mail: Lucifermonao@gmx.de
