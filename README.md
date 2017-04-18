# mini_qa
**A mini factoid based question answering system.**
    
    I.    mini_qa system begins when user forks a query.
    
    II.   The query is normalized and sent over the WikiPedia API.
    
    III.  The wikiPedia API return the set of documents under that query.
    
    IV.   Next to it the vector space search create a order of documents which are most relevant to the query.
    
    V.    Highest ranked document is selected for Information retrieval.