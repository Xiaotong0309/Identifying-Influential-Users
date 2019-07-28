# Identifying Influential Uers in Social Networks

### File organization:

#### Code

Network Project.ipynb - Main program to find influential users

net_Analyze.py - Preliminary: Analyze the property of social networks

webwebTest.ipynb - Draw graph of social networks

#### Report

Diao Xiaotong & Dong Ziyuan report.pdf

The other files are the experiment results and dataset

### Result

This repo tested 9 degree-based algorithms

Please check Diao Xiaotong & Dong Ziyuan report.pdf for detailed information

We found that Generalized_degree_discount is the best one for identifying influential user

### How to Use

To use the code as a tool to find influential user, you could

#### 1. Clean the data you have to the same format as [Gnutella p2p.txt](./Gnutella p2p.txt)
All users must have a unique identifier
Should have all connection information of all users

#### 2. Update the file name in Network Project.ipynb
Use your cleaned data as input

#### 3. Add the following code to show influential users identifier
```
print(Generalized_degree_discount(G, p, l))
```

