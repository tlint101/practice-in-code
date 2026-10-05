---
title: "⚠️Marimo Widget Issues!"
subtitle: "Where I Try to Debug My Blog"
author: "Tony E. Lin"
date: "2026-10-06"
categories: [Coding, Marimo, Python]
---
# Bug Found
I noticed a bug on the last post I made on [2026.10.02](https://tlint101.github.io/practice-in-code/posts/25-marimo-widgets.html). 
The Marimo widgets work when I render the blog locally. It is when I upload them to the GitHub repo that I get these 
issues. None of the widgets are rendering!

## Trying to Debug
Recently, I have access to Claude. I thought this would be a good chance to test how to use this in my own workflow. I 
pointed it to my repo and gave it a link to the live blog and asked it for advice on how to debug the issue. Two things
happened:

1) I got an explanation about what is causing the problem. 
2) I still have no idea how to fix it.

## The Bug Explanation
So what is the problem? Apparently there is something called a Pyodide package, which allows Python packages to run in 
the browser. So obviously there is a broken link between my python environment and what Pyodide can render. It is 
frustrating. There are a few workarounds that I was given, but none of them are to my liking. That means I will need 
to live with this issue for the foreseeable future.    

# Conclusion
That is where I am right now. As excited as I was to be able to use Marimo for my posts, if I am unable to render the 
cheminformatic related widgets, then it doesn't seem like there is a point to continue on. It is a shame, because the 
interactivity is a great way to share information. 

I'm sure I can fix this in the future. It just takes time and persistence. Right now I don't have the time. And I don't 
feel like it is right to through an LLM to fix this problem either. **_I need to know what the problem is_** anyway. I 
just need to find the time for that first.  

In the meantime, the post will still be up to show the whole internet how my posts are broken. 

Things are still under construction here, okay? 😅