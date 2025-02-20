# block1-data-infrastructure

Final Projects
Netflix recommandation engine 📽️
600 min
Context 📇

With over 221.6 million subscribers worldwide, Netflix has become one the leading video streaming platform in the world. Founded in 1997, the company counts almost 4000 movies and 2000 TV shows on their platform.

With such a position comes a lot of ambition. Facing the new competition with Disney+, Prime Video and all the other streaming platforms, Netflix promised its investors that the company will manage to grow its number of subscribers (already very high).

This is a very interesting challenge and one of the way Netflix is tackling is by leveraging data. Netflix believes that a great recommandation engine would keep their users entertained and therefore making them stay on the platform and attract new subscribers.
Project goals 🎯

Your goal as a team of Machine Learning Engineers is to:

    Create a recommandation engine using any AI library that you know of.
    Create an infrastructure that ingest real-time user interactions on the platform.
    Automatically produce real-time recommandations after a user finished a movie.

Where to get data

To achieve this project, you will need to get access to some data! Here are two data sources that you can use:

    Netflix Prize Data
        This dataset contains a large amount of payments labelled as fraudulent or not
        Read the work that some great data scientists have already done. We particularly enjoy this one
        Build your algorithm based on their work
        Then use your algorithm within your infrastructure to create a real-time recommandation engine! ⏩

    Jedha x Netflix real-time user interactions API
        This API retrieves real-time movie watched
        Use this to create real-time predictions

Deliverables 📬

To complete this project, you will need to produce:

    A schema of the infrastructure you chose to build and why you built it that way
        This can be in a Powerpoint, Word document
        You can get inspiration from the below picture crack

    The source code of all elements necessary to build your infrastructure

    A video of your working infrastructure on an example
        You can use Vidyard to do so

Tips 🦮

To help you in your task, we would like to give you a few tips on how to tackle that project.
How can I build the algorithm?

To build you algorithm, you can use any library (sklearn, tensorflow), APIs or even No-code tools.

If you don't want to build the algorithm yourself, feel free to use AmazonML, which is a great API tool. Check out our online-course on the matter

Remember to build something that is reusable! Especially in terms of preprocessing, using an algorithm is not only about using a .predict() 😉
I don't know where to start

First things first, in this project you need to at least:

    Train an algorithm
    Stage in to production
    Store real-time data in a db

This is our recommandation on where to start:

basic_infrastructure
IMPORTANT

The above example is just a suggestion, you can deviate from this infrastructure. The only minimal elements we need to have are:

    An element collecting & storing data
    An element consuming data
    An ETL (or ELT) process

How do I split work among my teammates?

Working together is key here! You can split your work several ways, but here is a suggestion:

    One team member can train the algorithm
    One team member can build MLflow infrastructure
    One team member can create the real-time data ingestion pipeline
