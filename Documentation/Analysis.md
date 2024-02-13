# Simplified Attendance with AWS

## The problem
The traditional attendance taking model is grossly inefficient. Teachers meticulously call each student by name, and students must listen for their names and verbally notify the teacher of their presence. This process wastes unnecessary time for both students and teachers alike.

## Our solution
We seek to totally revamp the way educators take attendance. Instead of teachers wasting time calling students by name, we plan to place a card scanner at the entrance to a classroom. Students will simply scan their student ID card upon arrival to submit their name to be counted present for the class. The names of students who’ve scanned in will be sent to a FERPA compliant website, to be accessed by the teacher. The website will display a simple, readable list of every student who scanned their ID when entering the room. Teachers can then conclude the attendance process as normal, marking the students who appear on the list present, and those not on the list absent.

## Technology to be used
Our card readers will consist of an RFID/NFC scanner module, and a Raspberry Pi machine, all housed neatly in a custom, compact enclosure. The Raspberry Pi will be connected to the cloud via AWS IoT Hub. When the card reader detects a card, it will be picked up by IoT Hub, which will cause Eventbridge to trigger a Lambda function that queries a DynamoDB database of student ID’s, and the names of the students that they belong to, and return the name of the student scanning in. The Lambda function then sends this value to an S3 bucket, to eventually be displayed on the website. According to FERPA guidelines, we must ensure that student data (names and ID’s) are kept safe from prying eyes and bad actors, this is done by encrypting the data behind an authentication system. Customer Identity Access Management (CIAM) is handled through AWS Cognito, requiring teachers to be registered in a Cognito User Pool to log in, and access the list of students scanning in.

## System architecture
![System architecture diagram](/Capstone_Diagram.png)