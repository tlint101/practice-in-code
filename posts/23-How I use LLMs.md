---
title: "How I use LLMs"
subtitle: "Where I Fear for My Job?"
author: "Tony E. Lin"
date: "2026-09-01"
categories: [Thoughts, Writing, Coding, Rants]
---
# How I Use LLMs

## Introduction
OpenAI made a splash in the fall of 2022 with the release of their GPT model. It was a monumental moment. Almost five 
years on and the intelligence of the state of the art (SOTA) models have made a drastic leap, changing how we use 
computers. 

To be clear, when I say “we” I mean computer nerds and coders. Because there are now tons and tons of LLM models to 
download and use offline on your own GPU servers - that is, if you can afford a good GPU. Each model gives varied 
results. 

Instead, I expect many are still using the popular offerings, which is ChatGPT, Claude, or Gemini, as chatbots. I 
don’t think a large population of users are connecting apps or have set up agents. 

Yet.

But the changes are coming for everyone. And it’s important to draw a line and explain how we use these AI models in our 
professional and personal lives.

## Models That I Use
I was lucky to nab an M4 Mac Mini with 32GB of RAM back in January before the Apple price hike (last month's updates have 
my head turned, but my wallet is empty...). In these six months I have discovered and experimented with local LLM models 
and agentic harnesses. There are several reasons why I prefer local LLM models. 

1. Running LLM models locally means that the information stays on my machines.
2. Costs of running models through providers have been expensive.
3. I wanted to learn, first hand, how LLMs work, how to fine-tune them, and how to deploy them. The goal would be to 
expand this to a larger workstation, allowing lab members access to their own local LLMs. 

## Do Models Help Me?
This is the trillion dollar question. My work is strictly dry lab. I code and analyze data, and build projects to 
explain my work to collaborators. Do the these models help me with that? 

Yes and no.

Despite being able to run local LLM models, the ones I can run on my (puny) machine are **not SOTA** level. I cannot 
"one-shot" my projects. I cannot even get it to write a proper script to generate molecular fingerprints and compare 
Tanimoto similarity scores between two molecules on the first try. It is important to remember that the LLMs I use can
write a bunch of code that _looks right_, but _does not run right_. 

That does not mean they are not useful. It means that I can get started "faster". It means that if I have an idea, I can 
launch my local LLMs to write the skeleton for my idea. I can dress it up later. I can ask the LLM/Agent that I am 
running to correct the code to get the output I'm looking for. That requires a couple of iterations and rarely is 
anything done in "one-shot".

Where these models shine for me is debugging my projects. I treat it as a documentation tool. While I still visit a 
module documentation page, I no longer need to hunt for specifics. I can query the LLM. Or I can feed it the 
entire documentation and my project before querying my model directly. It has changed the way I troubleshoot my 
works. I would argue, for the better.

And it has also changed the way I ingest information. I've been following Karpathy's LLM-Wiki model ([I recommend this 
tool](https://github.com/SamurAIGPT/llm-wiki-agent/tree/main)) to build personal knowledge bases. I can tailor that for 
specific topics and build on them as I find new papers or blog posts. It is very neat and I find the information 
helpful as research in our field moves faster and faster.

## Still Writing
I still find myself writing a lot of my code, but the way I debug my issues have changed. The way I start a project has 
changed. The way I approach my projects have changed. But most important, I still put a heavy emphasis on my project 
structure. 

**That last point is important to me**. SOTA models have obviously changed programming. There are countless blogs and 
posts about a programmer setting up agents to talk to each other throughout the day, or a whole team now run by a single 
programmer with unlimited tokens building who can build custom tools to solve a problem at their company. A recent post 
by Pat Walters has a short discussion on how he benchmarked different models using Claude on his own linux system 
([read here](https://patwalters.github.io/Let-the-Agents-Do-the-Benchmarking/)). More power to them. 

I've not experienced that yet. Maybe the models I'm using are too dumb. Maybe I'm not as imaginative as I thought, and 
I'm limited by my hardware. Maybe I am in denial. I am self-taught after all. 

As impressed as I am about LLMs, and local LLMs in particular, none of my experience has shown me that I am fully 100% 
replaceable. Not yet. More than ever, fundamentals remain just as important now as it did back in the 1950s. **_A project 
must remain manageable_**. I don't think fully passing a project for an LLM to build is wise. At least with this current 
model generation. I find that they continue to build large scripts and functions that lack proper organization in class 
structures. Worse, they often break or run incorrectly. Relying on LLMs for this will only increase [technical debt](https://en.wikipedia.org/wiki/Technical_debt). 
And I hate technical debt...

That means for now, if given the opportunity to mentor junior members, **I will continue stressing project structure**. 
I will query why they used a list instead of a dictionary, or why a script contains a series of functions instead of a 
class. I cannot have them pass off project structure to LLMs. Cause if they do that, then why even get into our field 
in the first place?

Many in academia, at least in the country I am in, are forgetting that. It's a shame. New students need someone to guide 
them. Now, more than ever. In the search for grants and funding, many have that. 

#### A Small Rant
As I was writing this post, I noticed it turning into a long rant. What I kept does not touch on my feelings 100%, but 
it's a start. I felt it is important to air out some of my personal grievances first.

Like everywhere, the country I do my research in is looking to build and incorporate AI tools throughout. It is a 
double-edged sword. The powers at be put pressure on fast buildout and results. Unfortunately, the advancement of LLMs 
and agentic coding is happening so fast that academia in the country I am in lack experts in the field. Without proper 
training and knowledge of the algorithms, how does one gauge model performance? This results in review committee members 
with a simple mindset. All they want to see are simple Accuracy, Precision, or R<sup>2</sup> results. While important, 
rarely do these metrics tell the full picture of a model’s performance. 

All of this results in students/trainees without the skills to build a solid project. Little emphasis is on modules, 
the project buildout, or the future maintenance of the project. Instead, "benchmaxing" a favorable Accuracy or 
R<sup>2</sup> value is all that is needed to get grants, awards, or praise. Explaining the project production is a waste 
of time to many.

The truth is that it is incredibly difficult that a coding project in academia can be converted and deployed to 
production level. But review committee members, and others in my country's academia, think this can be waved away 
like magic using LLMs and agents. 

I cannot, and will not, work that way. To me, it is important to understand the structure of my projects. Only then does 
it make deployment easier - easier to add features, easier to write, easier to maintain. Building a model with good 
Accuracy, Precision, or  R<sup>2</sup> values is not that difficult (depending on the target dataset). ***Building a project*** 
that you can use ***over and over*** and maintain over time is the wall everyone has to scale. That is key. 

This idea is what has influenced my workflow. For better or worse, it is a hill I am willing to die on. And for any 
junior members I mentor, I will always stress this to them. Whether I last long enough in this country's academia will 
be a question for another time.

# Final Thoughts
What LLMs have done is given tools to more people. We can build custom programs to solve our personal problems. That is 
great! Unfortunately, as our programs scale, then things start to fall apart. LLMs do not understand project structure. 
We have to instruct it. We have to guide it. **_We have to know what we want_**. Or at least, we need to know what 
problem we are trying to solve  

Maybe one day we will get a local LLM model, or even a SOTA model, that can "one-shot" an entire 
Design–Make–Test–Analyze/Decide (DMTA) cycle for drug development. Perhaps we are close. But not today. 

All of this to say that one thing will always remain constant - _**Know the Fundamentals**_! It is important. It will 
always remain important.