# Process-Network Interface

# A socket is a software interface used by the process to send messages into and receive messages from the network.

# A software interface that helps the developer to interact with the network…essentially an API!

# A developer has full control of the application layer side of the socket But he has little control of the Transport-Layer side of it.

# The only control the application developer has on the transport-layer side is the choice of transport protocol and the ability to fix a few transport-layer parameters such as maximum buffer and maximum segment sizes.

# .NET Framework (C#) -->
# Golang(Go) --> Concurrency in mind
# ---> Why concurrency?


# TCP vs. UDP
# TCP --> Welcoming Socket!
# HTTP --> 80 ---> Connection to a random port
# Clinet --> 80 ---> New socket ----> Client --> New Socket
# 
#UDP ---> A single socket 
