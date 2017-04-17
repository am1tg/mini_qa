# mini_qa
A mini factoid based question answering system.
    > mini_qa system begins when user forks a query.
    > The query is normalized and sent over the WikiPedia API.
    > The wikiPedia API return the set of documents under that query.
    > Next to it the vector space search create a order of documents which are most relevant to the query.
    > Highest ranked document is selected for Information retrieval.