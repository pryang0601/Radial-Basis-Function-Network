# Radial-Basis-Function-Network
## RBFN Homework from Neural Network Course in National Central University
### Language: Python
### GUI tool: wxPython

Users can use the GUI to choose the dataset in the <b>Dataset folder</b>: train4dAll.txt or train6dAll.txt.</br>
"軌跡座標點" is the x-y point in the graph</br>
Press the "RUN" buttom to start the training process.</br>
After training, users can see the car simulator(circle) in the left side of the GUI.</br>
System will record the trace of the car in the "track4D.txt" and "track6D.txt"(in the Result folder)</br>
<ul>
  <li>kmeans4d.py is for initializing the parameters for RBFN4d.py</li>
  <li>kmeans6d.py is for initializing the parameters for RBFN6d.py</li>
</ul>

You can see the result of "gif" format file in the <b>Result folder</b></br>
In the results, users can see:
<ol>
  <li> Direction: based on the front set as 90 degree, turn right as positive, turn left as negative</li>
  <li> Front Distance: the distance between the car's current degree's front wall and the car</li>
  <li> Right Distance: the distance between the car's current degree's right 45 degree's wall and the car</li>
  <li> Left Distance: the distance between the car's current degree's left 45 degree's wall and the car</li>
 </ol>
For example:</br>
<img src="https://upload.cc/i1/2023/01/03/JKAegt.png" alt="car" width=300 hight=250>
