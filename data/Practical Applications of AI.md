# Practical Applications of AI
## Three useful use-cases of AI. Waterstons Innovation: The Dots #18

In the last few weeks, we have written about how AI is expensive and uncreative, and about the areas where it shouldn’t be used. However, we also believe there are a lot of good use cases out there if we are thoughtful about it. This week, we will discuss some of them, and begin to hash out some ideas for criteria for what makes a good AI project.

What is this? This is The Dots, our newsletter about exciting things we find in the world of innovation. We imagine innovation as connecting the dots; putting together a jigsaw. Our puzzle pieces are the pieces of interesting information we absorb in the world, our partners and their products. Innovation happens when we connect these pieces in new and interesting ways. This newsletter is about these dots we find and connect.

### Alex
Google Deepmind recently announced that they’ve created an AI-based weather forecasting model that outperforms existing models 99.7% of the time (maybe now the Mirror and the Sun can be even more positive that we’re going to have the coldest, snowiest, most treacherous winter on record).

Forecasting the weather is notoriously difficult, especially anything more than 24 hours in advance. Weather forecasting models have long been used to illustrate the impact of chaos theory - a tiny change in the wind pressure in Alabama can change the forecast in Colorado from beating sunshine to hammering hail.

Weather forecasting has also traditionally been very slow with the ten-day forecasting taking hours of supercomputer time to process. GraphCast, however, manages higher accuracy in less than a minute. The technical magic at the heart of all this is the transformer.

Transformers are the basis of most modern “AI”. They're remarkably versatile - ChatGPT, Midjourney, AlphaFold and AlphaStar all use transformers despite seeming like they’re all solving completely different problems. You can imagine a transformer as a kind of very smart, very flexible translator. They can translate from one language into another but they can also translate from information into instructions or from instructions into images, video, gaussian splatted point clouds or emails to your boss explaining why you need a pay rise.

ChatGPT is the LLM you know and love - you give it words and it transforms those into more words. AlphaFold is Google Deepmind’s tool for protein folding (and probably one of the most important and yet unknown uses of AI there is) AlphaFold transforms models of unfolded proteins into folded proteins in three-dimensional space. AlphaStar is Deepmind’s AI that plays the classic strategy video game Starcraft. AlphaStar uses transformers to turn its understanding of the game world into instructions to execute.

I’m incredibly excited to see where this technology goes. Clearly having CoPilot rewrite all the emails your business sends for 30 grand a month is just the tip of the iceberg. Transformers are going to end up being used for route planning, resource optimisation, designing better factory layouts and who knows what else. If you use data or observations to inform decisions and you have a lot of historical data documenting how you’ve done that in the past then transformers might be able to help!

### Andrew
While there can be a desire to adopt a tool because it's exciting and new (I know I feel that), there should be a consideration on how to ground it in a project that will make a difference. A good AI project should be based on an actual challenge you face, and led by that. But, how do you begin to find an appropriate challenge? Where do you start? You probably face a range of issues in your sector, many will be appropriate for AI to solve, and many inappropriate.

I've been trying to come up with a list of generic questions on how to spot a good AI project (and some examples of what those might be). This is my first draft:

Does this thing go wrong a lot? I am getting a lot of warranty returns, what is the root cause? A lot of students are dropping out, what is contributing to this? This machine keeps breaking, can you tell me when it will break next?

I know what happened last time, but what will happen next? This could be predicting your finances for the next quarter, understanding how many students will show up to your university next year, or if a project is going to fail

Is something in the wrong place? What about using cameras - is there a person in a dangerous area of a factory? Can you spot a burned cookie in a pile of nice ones (a real problem we have seen) Or, maybe there is a car in your company car park there shouldn't be.

We do this a lot, and I hate doing it. Can I make it stop? Think about the boring admin tasks you always have to do. Can I use AI to write documentation? Or extract information from the receipts I have to file at the end of the month? Given the skills of my staff, and how every previous project went, what's the best way to resource the next project?

I know what good looks like, can I stop it from going bad? You know how the saw in your factory normally behaves, can you be alerted as it starts to behave differently? When you are designing a building you know how long it should take to get through the different design stages, can you tell me when something is taking too long?

What unites these is the availability of data - specifically, your data - and using it to inform decision-making.

I think they could use some polishing, but what do you think of my list of questions? Have I missed something? Let me know what you think!

### Katie
Automating time-consuming and repetitive tasks, such as submitting expense reports can be easily achieved using AI. Azure’s document Intelligence allows you to read receipts and extract information such as the total amount, number of items and Merchant name. This information can be used to populate forms using a tool called Power Automate, which could save staff a significant amount of time each month.  

Why do this?

Receipts are not the most fun activity to complete every month.

Allows staff to focus on other areas of their job they enjoy.

Hopefully, save the finance from chasing everyone to fill in their expense report.

How I did do it?

Phase 1 of this project allows an employee to email their receipts to a dedicated email address. When an email is sent, this saves all the attachments to Sharepoint in a file under their name. When it is time to complete the expense report, the receipts are passed through Azure document intelligence, which obtains the total amount and the merchant’s name. This is matched to an expense line in Excel and the path to the documents are added to the table. The file is renamed to match the expense line, making it quicker for staff to complete their expense report.

Phase 2 will involve using Power Automate to automatically complete our staff expense reports on our CRM, including updating images, and using prompt engineering to include descriptions and categorise receipts.

Where else could this be applied?

Updating documents/forms that follow a specific template

Writing up documents that follow a specific template

Automating repetitive tasks that you need to complete either daily, weekly or monthly



### You Might Have Missed It…
Best printer 2023: just buy this Brother laser printer everyone has, it’s fine - here is The Verges’ list of best printers of 2023. The list has a very good point: why are we wasting our time thinking about printers?


### The Next Start-Up Unicorn,
An advent calendar, that every day gives you 1/25th of your Christmas dinner. By Christmas day, you now have all the ingredients you need! No need to go to a busy Tescos!

