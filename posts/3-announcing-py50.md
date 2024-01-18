---
title: 'Announcing py50!'
author: 'Tony E. Lin'
date: '2023-12-05'
categories: [Python, Streamlit, py50, Coding, Informatics, Plotting]
image: 'img/py50_logo_only.png'
---

### py50: Generate Dose-Response Curves

I would like to announce a new project I have been working on: [py50: Generate Dose-Response Curves](https://github.com/tlint101/py50). 
It is the first "big" python project that I have worked on. This package will calculate IC50 (py50, get it? ... Anyone?) 
and will plot the dose-response curves. And for anyone who does not know how to code, I created a Streamlit web 
application([click here](https://py50-app.streamlit.app)). I hope others will be able to find this useful for their own 
work. 

#### Why did I make py50?

Well, this was mostly for myself. I am lucky to be in a lab that has close collaborations with other labs, meaning that my work
can quickly be shared with experts in other areas. They will generate the dose-response curves for me. But sometimes 
when I organize my figures, I realized that the curves do not fit my style. The color does not match my docking pose,
or my protein, or the font could be bigger, etc. Now, I could ask them to change it, but I do not like to be a burden on
people. They spent a lot of time doing this work, the least I could do is learn the program they used to generate plot, right?

Well, the truth is I hate using their program (which I will not name here)! 

So I went about creating my own. As a python module, it can be customizable to anyone's workflow. The outcome is perfect
for me. After I showed this to my advisor, he made the comment that it would be good for others to use. And I realized 
that I could easily convert the code for this purpose. 

For py50, I have a KNIME workflow. That is available upon request. It is not as elegant, as they are not custom KNIME nodes, 
so I am a little more reserved in sharing that workflow. Another issue with KNIME is that it would require the user to have 
python installed on their machine. I realized that could be a hassle. So I also created a Streamlit web application. 
Using Streamlit has been on my list of things to try for a very long time, and I am glad that with my py50 project, I 
was able to do that.

The code is not perfect. There is a lot that I need to clean up on the backend. But for what I have, it works and I learned 
a lot. I am very surprised I got a decent package up and running. The plan is to maintain this for the foreseeable future. 
And, if the inspiration is right, I will add some extra features over the coming years. 

The next few posts will dive into details about py50, the functions, and concepts of IC50 that I ran into. 
