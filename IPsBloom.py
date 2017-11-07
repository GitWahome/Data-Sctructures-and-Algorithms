#Non cryptographic hash functions package
import pyhash
import random
def bloomIPs(clientSize):
    """
    I will implement the IP blocker above example.
    For simplicity, lets assume our IP system is composed of values between
    0-100000
    """
    #My bit vector
    bitVector=[0]*clientSize

    """
    We use 3 hash functions, Murmur, FNV and metro hash systems. They are 
    non cryptographic hence will return the same value any time we pass in
    the same value. We modularize them by our bit  Vector size to make them
    fit into it as it is our reference sheet.
    """
    fnv=pyhash.fnv1_32()
    murmur=pyhash.murmur3_32()
    metro=pyhash.metro_128()

    """
    Now lets imagine we identified a set of just 1000 hackers in our world.
    Their IPs range from 0 to 1000 as follows.
    """
    hackerSize=1000
    hackersList=range(0,hackerSize)
    """
    To keep our random clients happy, we come up with a repo of all the 
    hackers Known. Our customers are very stubborn but they love being safe.
    Its a very dangerous world out there.
    We mark the hackers.
    """
    for hacker in hackersList:
        #Hash them with our 3 functions
        bitVector[fnv(str(hacker))%clientSize]=1
        bitVector[murmur(str(hacker))%clientSize]=1
        bitVector[metro(str(hacker))%clientSize]=1
    """
    Now our true clients make requests. We have say 100000 of them.
    We look them up in our list and determine if they are hackers or not
    An approved request is marked as Perfect. Lets count, of the 700,
    False Positives are clients Noted as Hackers
    How many will be marked perfect
    """
    perfect=0
    falsePositive=0
    for cust in range(0,100000):
        trueClient=random.randrange(10000,100000)
        check1= bitVector[fnv(str(trueClient))%clientSize]
        check2=bitVector[murmur(str(trueClient))%clientSize]
        check3=bitVector[metro(str(trueClient))%clientSize]
        #print("{}-{}-{}").format(check1,check2,check3)
        """
        We will not grant perfection to them if they are detected as hackers
        by any of our security systems, we mark the false positive.
        Othewise we just think of them as false negatives
        """
        checkFinale=(check1==check2==check3==1)
        if checkFinale is True:
            falsePositive+=1
        else:
            perfect+=1
    doc="""
    Running our check, we wil throw warnings to some true clients thinking
    they are hackers when they are in fact not. Run it again to see how
    many true clients connect. At least we know they are safe. But as seen.
    there is a possibility of our clients, whose IPs are not even in the
    same range as the hackers to be detected as hackers."""
    return {"hackerSize":hackerSize,
            "falsePositive":falsePositive,
            "clientSize":clientSize,
            "doc":doc,
            "perfect":perfect}
resNow=bloomIPs(10000)
print("**********WELCOME TO BRIAN'S WORLD***********")
print("Brian's world has a total of {} hackers").format(resNow["hackerSize"])
print("\n{} true customers were marked hackers:-(").format(resNow["falsePositive"])
print("But, {} true customers connected perfectly:-)").format(resNow["perfect"])
print(resNow["doc"])
