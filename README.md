# AttenEase PiCloud
We seek to automate the attendance taking process by allowing students to scan their student ID card upon entering a classroom, sending their name to a web application that shows the teacher a simple list of everyone who's scanned in.

## Who Are We?
 ***Team JZRJ*** (catchy, right?)
 - Jacob Plaziak - *jmplaziak*
 - Zach Redland - *zachary-redland*
 - Richard Phann - *pharicDunwoody*
 - Jake Hochstatter - *FlyxHub*

## Project Blueprint
Most current diagram of what our solution will look like:

![Current project diagram](Capstone_Diagram.png)

## Hardware checkout
Like a library, but for hardware!

|Item|Team member|
|:-:|:-:|
|Card Readers|Jake H.|
|Raspberry Pi|Zach R.|

## Shopping List
List of things we need to buy for the project:

| Item | Cost |
|-|-|
|Running total | **$0.00** |

## Purchase Orders
Where's my stuff?

|P.O.|Item|Status|
|-|-|-|
|1|[HiLetgo RFID Card Reader](https://www.amazon.com/HiLetgo-125Khz-EM4100-Reader-Swipe/dp/B01MZYYDUV/ref=sr_1_3?keywords=RFID+Readers&qid=1707835660&sr=8-3)|Arrived|N/A|
|1|Mystery NFC Reader|Arrived|
|2|[Raspberry Pi Zero W](https://www.amazon.com/Raspberry-Pi-Zero-Wireless-model/dp/B06XFZC3BX/ref=asc_df_B06XFZC3BX/?tag=hyprod-20&linkCode=df0&hvadid=312363697617&hvpos=&hvnetw=g&hvrand=12255993669550297530&hvpone=&hvptwo=&hvqmt=&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=9019669&hvtargid=pla-405706373744&psc=1&mcid=7c324a0a86243324915c51bfb077f963&tag=&ref=&adgrpid=61916342293&hvpone=&hvptwo=&hvadid=312363697617&hvpos=&hvnetw=g&hvrand=12255993669550297530&hvqmt=&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=9019669&hvtargid=pla-405706373744&gclid=Cj0KCQiAqsitBhDlARIsAGMR1Rh3R2iQx6Wp9i3mGJZ7Fr_0tgGDG1drqlVJABb0oX2EUVb8bdxf-iMaAvdREALw_wcB)|Arrived|
|2|[SanDisk 32GB MicroSD Card](https://www.amazon.com/SanDisk-Ultra-SDSQUNB-032G-GN3MN-UHS-I-microSDHC/dp/B010NE3QHQ/ref=sr_1_21?crid=2G088BBQ62KN5&keywords=microSD+card&qid=1707407180&s=electronics&sprefix=microsd+card%2Celectronics%2C200&sr=1-21)|Arrived|
|3|Cloud Resources|Arrived|
|4|[Sony RC-S380](https://www.amazon.com/Sony-RC-S380-PaSoRi-Card-Reader/dp/B00VR1WARC)|Arrived|

## To-Do List
What can I be doing right now?

- [x] Get card reader ordered
- [ ] Experiment with card reader(s)
  - [X] Write nfcpy script
    - [ ] Figure out how to connect to AWS
- [x] Research Raspberry Pi
- [x] Order Raspberry Pi
- [x] Configure OS and network on Pi
- [ ] Setup IAM accounts for team members in AWS environment
- [ ] Connect card reader to Pi, configure Pi to send values to AWS
- [ ] Build data pipeline in AWS
- [ ] Set up Cognito user pool?
- [ ] Build DB(s)?
- [ ] Build web application to read from data pipeline
- [ ] Design final blueprint
- [ ] Design and 3D print housing for Pi/reader
- [ ] Present
  - [ ] Slide deck/Demo video?
