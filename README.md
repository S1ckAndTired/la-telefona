# la-telefona
<p align="center">
<img src="https://user-images.githubusercontent.com/78124142/172986719-cf6213c1-1241-4b84-9552-42c97ac99e60.gif" />
</p>

#### What is la-telefona?
la-telefona is a python script aimed to enumerate users based on their phone numbers.

#### How should be used?
The script is get request based. If the web app you're testing has a function such as "resend PIN code" and once you send a non registered number, the status code of the page is different from when you send a valid one, in theory you could enumerate users based on this. That's why this script was built.

#### If you get some hostname error, run this...
  pip install urllib3==1.25.11
