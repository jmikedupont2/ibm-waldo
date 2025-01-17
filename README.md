WALDO
======

Introduction
------------

People with learning disabilities can encounter difficulty in expressing themselves in speech. Makaton is a language programme that uses signs and symbols to enable users of all ages to communicate effectively. WALDO is a machine learning-enabled assisted living device meant for use by Makaton users and their carers in a care home setting. WALDO’s capabilities include:

* Makaton sign language interpretation using machine learning
* Easy-to-use interface, and a cute and endearing package to encourage use by people with learning disabilities and their carers
* Programmable buttons for users to quickly express pre-set phrases or emotions

Intended Use
---

WALDO is intended for use in a care home setting in the following ways:

Makaton sign interpretation
1. Makaton user (care home patient) signs to WALDO
2. WALDO uses machine learning to interpret sign
3. WALDO vocalises sign for carer to understand what user intends to express
4. Carer reacts accordingly, completing the interaction between the user and carer
This implementation enables the carer to understand the user without having to undergo the time-consuming process of learning Makaton.

Expression of pre-set phrases/emotions
1. User (by him/herself, or via carer) sets common phrases that he/she uses frequently to correspond to physical buttons on WALDO
2. User labels buttons accordingly for ease of use
3. User presses the relevant button, WALDO vocalises pre-set phrase
4. Carer responds accordingly
This implementation enables people with learning disabilities that have difficulty expressing themselves in speech to easily express everyday sentiments.


Virtual Design History File Overview
---

This is an overview of the various sections and subsections of WALDO's Virtual Design History File (VDHF). The VDHF details the developmental process of WALDO, the necessary steps to recreate it and the ethical and sustainability considerations of WALDO.

<table>
  <tr>
    <th width="18%">Section</th>
    <th width="22%">Subsection</th>
    <th>Description</th>
  </tr>
  <tr>
    <td colspan="2"><span style="font-weight:bold">Overview</span></td>
    <td>Overview of WALDO, contents of Virtual Design History File</td>
  </tr>
  <tr>
    <td rowspan="3"><span style="font-weight:bold">1. Setup</span></td>
    <td> <a href="https://github.com/patrickjohncyh/ibm-waldo/blob/master/1-Setup/1-1-Jetson-Setup.md">1.1 Jetson Nano Setup</a></td>
    <td>Jetson Nano Setup Guide</td>
  </tr>
  <tr>
    <td><a href="https://github.com/patrickjohncyh/ibm-waldo/blob/master/1-Setup/1-2-Pi-Setup.md">1.2 Pi Setup</a></td>
    <td>Raspberry Pi Setup Guide</td>
  </tr>
  <tr>
    <td><a href="https://github.com/patrickjohncyh/ibm-waldo/blob/master/1-Setup/1-3-Hardware-Connections.md">1.3 Hardware Setup</a></td>
    <td>Diagram of device hardware connections</td>
  </tr>
  <tr>
    <td rowspan="5"><span style="font-weight:bold">2. Machine Learning</span></td>
    <td><a href="https://github.com/patrickjohncyh/ibm-waldo/blob/master/2-MachineLearning/2-1-Machine-Learning.md"> 2.1 Machine Learning </a></td>
    <td>Details model design history and evolution as well as implementation on the edge device</td>
  </tr>
  <tr>
    <td><a href="https://github.com/patrickjohncyh/ibm-waldo/blob/master/2-MachineLearning/2-2-Server-Environment-Setup.md"> 2.2 Server Environment Setup</a></td>
    <td>Setting up server environment for further model training</td>
  </tr>
  <tr>
    <td><a href="https://github.com/patrickjohncyh/ibm-waldo/tree/master/2-MachineLearning/server-training"> Server Training Code</a></td>
    <td>Code to be run on server for model training</td>
  </tr>
  <tr>
    <td><a href ="https://github.com/patrickjohncyh/ibm-waldo/tree/master/2-MachineLearning/jetson-execution">Jetson Nano Execution Code</a></td>
    <td>Code to be run on Jetson Nano for Makaton sign recognition</td>
  </tr>
  <tr>
    <td><a href = "https://github.com/patrickjohncyh/ibm-waldo/tree/master/2-MachineLearning/jetson-execution/checkpoint_models"> Model and Weights</a></td>
    <td>Saved weights of the final trained model</td>
  </tr>

  <tr>
    <td rowspan="4"><span style="font-weight:bold">3. Raspberry Pi</span></td>
    <td><a href="https://github.com/patrickjohncyh/ibm-waldo/blob/master/3-Pi/3-1-Pi-Function.md"> 3.1 Overview of Pi Function</a></td>
    <td>Outline of functions and connections of Pi</td>
  </tr>
  <tr>
    <td><a href="https://github.com/patrickjohncyh/ibm-waldo/tree/master/3-Pi/pi-execution"> Pi Execution Code</td>
    <td>Code to be run on Raspberry Pi for high level tasks and audio generations through the IBM Watson text to speech module</span></td>
  </tr>
  <tr>
    
  </tr>
  <tr>
    
  </tr>
  <tr>
    <td rowspan="3"><span style="font-weight:bold">4. Hardware</span></td>
    <td><a href="https://github.com/patrickjohncyh/ibm-waldo/tree/master/4-Hardware/4-1-3D-Printing-STL-Files">4.1 3D printing files</a></td>
    <td>Contains Standard Tessellation Language (STL) files of the Jetson Nano case, the Pi case, the button support structure and WALDO’s eyepiece</td>
  </tr>
  <tr>
    <td><a href="https://github.com/patrickjohncyh/ibm-waldo/blob/master/4-Hardware/4-2-Power-Supply.md">4.2 Power Supply</td>
    <td>Summary of considerations when choosing WALDO’s power supply</td>
  </tr>
  <tr>
    <td><a href="https://github.com/patrickjohncyh/ibm-waldo/blob/master/4-Hardware/4-3-Hardware-List.md">4.3 Hardware List</td>
    <td>List of all hardware components used in assembly of WALDO</td>
  </tr>
  <tr>
    <td rowspan="4"><span style="font-weight:bold">5. Administrative</span></td>
    <td><a href="https://github.com/patrickjohncyh/ibm-waldo/tree/master/5-Administrative/5-1-Record-of-Meetings">5.1 Record of Meetings</td>
    <td>Meeting minutes and decisions made</td>
  </tr>
  <tr>
    <td><a href="https://github.com/patrickjohncyh/ibm-waldo/blob/master/5-Administrative/5-2-Gantt-Chart.md">5.2 Gantt Chart</td>
    <td>Intended timeline of project (plotted during first meeting at IBM Hursley)</td>
  </tr>
  <tr>
    <td><a href="https://github.com/patrickjohncyh/ibm-waldo/blob/master/5-Administrative/5-3-Bill-of-Materials.md">5.3 Bill of Materials</td>
    <td>Record of expenditure and outline of cost of device</td>
  </tr>
  <tr>
    <td><a href="https://github.com/patrickjohncyh/ibm-waldo/blob/master/5-Administrative/5-4-Data-Collection.md">5.4 Data Collection</td>
    <td>Outline of procedure, considerations and product of data collection</td>
  </tr>
  <tr>
    <td rowspan="6"><span style="font-weight:bold">6. Miscellaneous</span></td>
    <td><a href="https://github.com/patrickjohncyh/ibm-waldo/blob/master/6-Miscellaneous/6-1-Ethical-Considerations.md">6.1 Ethical Considerations</td>
    <td>Outline of ethical considerations in the design, building and use of WALDO</td>
  </tr>
  <tr>
    <td><a href="https://github.com/patrickjohncyh/ibm-waldo/blob/master/6-Miscellaneous/6-2-Sustainability-Considerations.md"> 6.2 Sustainability considerations</td>
    <td>Outline of sustainability considerations in the design, building and use of WALDO</td>
  </tr>
  <tr>
    <td><a href="https://github.com/patrickjohncyh/ibm-waldo/blob/master/6-Miscellaneous/6-3-Blog.md">6.3 Blog</td>
    <td>Rationale behind the blog and links to the blog posts</td>
  </tr>
  <tr>
    <td><a href="https://github.com/patrickjohncyh/ibm-waldo/blob/master/6-Miscellaneous/6-4-Future-Work.md">6.4 Future Work</td>
    <td>Discussion of present implementation and possible extensions to the project</td>
  </tr>
  <tr>
    <td><a href="https://github.com/patrickjohncyh/ibm-waldo/blob/master/6-Miscellaneous/6-5-Leaflet.pdf">6.5 Leaflet</td>
    <td>Informational leaflet on WALDO</td>
  </tr>
  <tr>
    <td><a href="https://github.com/patrickjohncyh/ibm-waldo/blob/master/6-Miscellaneous/6-6-Poster.pdf">6.6 Poster</td>
    <td>Poster for hackbooth and presentation</td>
  </tr>
</table>

Acknowledgements
---

The WALDO team consists of 5 students from the Electrical Engineering (EE) Department of Imperial College London. The key tasks performed by each member is as follows,

1. [Joshua Chan](https://github.com/josh8chan) : Administrative, Data Collection, Peripheral Sensors Implementation 
2. [Lua Ying Hao](https://github.com/Kaynelua) : Jetson Nano Implementation, Machine Learning
3. [Ng Yi Song](https://github.com/NgYiSong) : Data Collection, Peripheral Sensors Implementation
4. [Patrick John Chia](https://github.com/patrickjohncyh) : Jetson Nano Implementation, Machine Learning
5. [Yeow En Kai Joel](https://github.com/joelyeow) : Administrative, Data Collection and Processing, Peripheral Sensors Implementation 

We would like to thank:

1. Dr Steve Wright, for his invaluable guidance and encouragement throughout the project
2. Louise Cooper, John McNamara & Emily Larkin from IBM for their clear direction and unwavering support in the implementation of this project
3. Precious Homes, for supporting this project by providing valuable insight into the use of Makaton, as well as training videos
4. Vic, May & Amine at the teaching labs, for their untiring technical support
5. All who volunteered their time to help us in the collection of training data

