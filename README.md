# RedisChat
A simple chat system based on Redis PUBSUB with encryption. This still needs more refining. I still have to work out the consesus part where all users can approve other users so that at a given time there aren't more than one user with the same username.
The entire working is also not perfect givent that this entire can be reworked into a UDP based P2P chat so as to have the entire system of a single redis server. 
Also there is no chat history. I have plans to implement that by mostly using Git to track them. Maybe the consensus can be done using a distributed ledger. But yes this was fun to try. 
Will most probably rewrite all of this in another language and solve the above issues
