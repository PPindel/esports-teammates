# Esports Teammates
![image](https://github.com/PPindel/esports-teammates/assets/114284732/30be1f01-4b22-45ff-9455-95161df96fea)

- Esports Teammates is a site created for people who like to play online, but couldn't find right teammates yet
- By creating a post, you can select your game, and describe your exerience, gaming skills and times preffered to play with your mates
- Easy to operate, easy to navigate, intuitive and well designed site for all gamers!

## Live Site
https://esports-teammates.herokuapp.com/

## Repository
https://github.com/PPindel/esports-teammates

## Author
Przemyslaw Pindel

# Table of Contents
🚀 **merit & beyond**

Generate after readme is complete by copying and pasting your readme from this point & below into this tool:
- [mardown table of contents generator](https://luciopaiva.com/markdown-toc/)
**NOTE:** It does have some bugs if you have dashes or trailing spaces in your headers, so make sure all these WORK!

# UX
## Target Audience
Esports Teammates is designed to be attractive to the gaming community.
It reflects the popular design of gaming accessories (illuminating leds for PCs, keyboards, mouses, etc.).
The site is easy to operate and navigate, the content is clear and users can communicate with themselves to find new online friends!

## Design Choices
### Colors
![image](https://github.com/PPindel/esports-teammates/assets/114284732/c0967ae8-0651-4f6b-8535-be232ec512e2)

The pallet inspiration was taken from coolors.co.
However, some of the colors had to be adjusted to match the contrast standard in the Lighthouse validator.

### Typography
Fonts used:
- Permanent Marker for modern and attractive design
- Ubuntu for clear and readable content

### Design Elements
The site has a common navbar (sticky to the top when scrolling), and footer.

![image](https://github.com/PPindel/esports-teammates/assets/114284732/e160e81d-07f4-4581-98c0-0ba1cbb484b4)
![image](https://github.com/PPindel/esports-teammates/assets/114284732/d604e5db-cefe-424b-a328-56ed0d9f2965)

Up to six posts per page, two rows of three posts for desktops, and one column for mobile phones.

![image](https://github.com/PPindel/esports-teammates/assets/114284732/a1bc8c5e-24a9-4d48-aa38-dc9c1bf73e1b)
![image](https://github.com/PPindel/esports-teammates/assets/114284732/60bdad1b-6473-4965-a7fb-cbae164b295d)

Landing page for not authenticated users:

![image](https://github.com/PPindel/esports-teammates/assets/114284732/3a38c9fb-76dd-4564-b91c-3ee9995a1ca3)

Buttons are changing colors when hovering over:

![image](https://github.com/PPindel/esports-teammates/assets/114284732/9ad37536-54e1-4608-8fc4-c655162a72dd)
![image](https://github.com/PPindel/esports-teammates/assets/114284732/eba8cb26-a89f-4147-b69f-fce54cc0c267)

All default Django pages (signup, login, etc.) are customised:

![image](https://github.com/PPindel/esports-teammates/assets/114284732/906e3e34-96da-4922-80e3-dca435e099d8)

Custom 404 and 500 error pages:

![image](https://github.com/PPindel/esports-teammates/assets/114284732/9621e955-8577-4f84-81ef-e5cc63612f3d)
![image](https://github.com/PPindel/esports-teammates/assets/114284732/031702af-1700-413f-8b42-0c3475748df3)

JS script for alerts:

![image](https://github.com/PPindel/esports-teammates/assets/114284732/a05ee5b3-523b-44d1-8896-f55e322a273c)

Simple profile page:

![image](https://github.com/PPindel/esports-teammates/assets/114284732/e874c26c-b37b-4668-a805-44f3b9f524d3)

Admin page:

![image](https://github.com/PPindel/esports-teammates/assets/114284732/1c2b2645-fa2d-4f64-ac6e-7346f6612fc6)

Link to my user stories:
https://github.com/users/PPindel/projects/4

### Frameworks, plugins, tools used
- Bootstrap
- Django
- req.txt:
  - asgiref==3.6.0
  - cloudinary==1.32.0
  - crispy-bootstrap5==0.7
  - dj-database-url==0.5.0
  - dj3-cloudinary-storage==0.0.6
  - Django==3.2.18
  - Django-Accounts==0.1
  - django-allauth==0.53.1
  - django-crispy-forms==1.14.0
  - django-summernote==0.8.20.0
  - gunicorn==20.1.0
  - oauthlib==3.2.2
  - psycopg2==2.9.5
  - PyJWT==2.6.0
  - python3-openid==3.2.0
  - pytz==2022.7.1
  - requests-oauthlib==1.3.1
  - sqlparse==0.4.3
  - django-extensions==3.2.1
  - graphviz==0.20.1


## Wireframes
Landing page:

![image](https://github.com/PPindel/esports-teammates/assets/114284732/69be5979-b6e4-4fa2-8a72-67d009b862ec)

Desktop site:

![image](https://github.com/PPindel/esports-teammates/assets/114284732/e2efaa7f-b4f1-468d-a260-57cc0e650a2f)

Mobile site:

![image](https://github.com/PPindel/esports-teammates/assets/114284732/8efc194f-ec88-4cf3-8e94-800d8cca3203)

Team detail page:

![image](https://github.com/PPindel/esports-teammates/assets/114284732/817847d3-29a1-48c5-b962-3d7067464dbc)

Register page:

![image](https://github.com/PPindel/esports-teammates/assets/114284732/54878dc1-0691-4db9-a5a5-7c9a0fa8c86d)

Some of the details were changed in final product.

# Information Architecture
## Entity Relationship Diagram
![image](https://github.com/PPindel/esports-teammates/assets/114284732/c246472a-40b9-4172-838d-bf5c0533515d)

## Database Choice
- postgres as the database because the data is relational
- heroku servers

## Data Models
Users can create and read their own Team Ad, select the title, game, role, skill level, write a description and upload custom image to the ad.

![image](https://github.com/PPindel/esports-teammates/assets/114284732/cd7e1773-fa8b-44ef-9e01-fa62dbdfcc31)

Unique slug generator function to prevent 2 identical slugs at the same time.

![image](https://github.com/PPindel/esports-teammates/assets/114284732/458a31f8-07f7-47f5-8293-07c0fbe95856)

Users can write comments under Team Ads.

![image](https://github.com/PPindel/esports-teammates/assets/114284732/0ad23a35-b1f3-4a19-920a-049a532018ec)

Users can also edit and delete TeamAds and Comments (only if they are the authors - access is protected).

![image](https://github.com/PPindel/esports-teammates/assets/114284732/52af4858-2fa7-4a72-8470-ad3e43bbd14d)

Default django signup form is slightly upgraded.

![image](https://github.com/PPindel/esports-teammates/assets/114284732/bbd833f2-f34f-4200-9904-17c9c35bccc8)

# Agile Process
## Project Goals
- users can create and read posts (TeamAds)
- users can edit and delete their posts
- users can comment created posts
- users can edit and delete their own comments
- admin can do all of the above for any post or comment

## Initial User Stories
https://github.com/users/PPindel/projects/4
All user stories are marked to show the importance.

![image](https://github.com/PPindel/esports-teammates/assets/114284732/13b9da32-d2ef-4de6-bec6-f98f219c21fa)

![image](https://github.com/PPindel/esports-teammates/assets/114284732/06993db0-9099-4a91-93b1-82aa83421655)

## Scope
When I started my project I was very ambitious to develop a complete portal for gamers to search online for friends, teams and improve their skills. I imagined custom applications, profiles, filtering tools, game sections, guilds, and many more...
But in the middle of developing, I realized that this may take much more time than I had to make it good.
I've created a functional website working similarly to a blog website where people can connect and make an advert. All previous ideas are still in GitHub user stories for this project.

# Features
🚨**Required** 

In this section, you should go over the different parts of your project, and describe each in a sentence or so and how they tie into  your user stories.

## Implemented Features
🚨**Required** 

It's easiest to break this section down into the header, footer, and each page/layer/signification section of your website. Call out any differences for mobile vs desktop presentations, include a screenshot of the implemented feature.

Don't forget your custom 404 error page

Don't forget the 3 phases of navigation:
- unauthenticated
- general authenticated user
- superuser authenticated

And don't forget Defensive programming bits
- validation of form inputs
- not allowing users to create, read, update and delete information they shouldn't

For some/all of your features, you may choose to reference the specific project files that implement them, although this is entirely optional.

## Future Features
🚀 **merit & beyond**

Use this section to discuss plans for additional features to be implemented in the future

If you end up not developing some features you hoped to implement, you can include those in this section too.

## Testing
🚨**Required** 

In this section, you need to convince the assessor that you have conducted enough testing to legitimately believe that the site works well. Essentially, in this part you will want to go over all of your user stories from the Features section and ensure that they all work as intended, with the project providing an easy and straightforward way for the users to achieve their goals.

If this section grows too long, you may want to split it off into a separate file and link to it from here.

**At this point, you should use gitHub Issues Templates** to track test cases and defects. Here's a [document](https://docs.google.com/document/d/1nDS5tZeMO77Dfq85IZGMSV6C41XaPm9FwcpR3k-UTVc/edit#heading=h.3kdbr3tqbzi) I put together for this process.


## Manual Testing
🚨**Required** 

For any scenarios that have not been automated, test the user stories/features manually and provide as much detail as is relevant. A particularly useful form for describing your testing process is via scenarios in markdown such as:

**Manual Testing For Contact Form**
1. Contact form:
    1. Go to the "Contact Us" page
    2. Try to submit the empty form and verify that an error message about the required fields appears
    3. Try to submit the form with an invalid email address and verify that a relevant error message appears
    4. Try to submit the form with all inputs valid and verify that a success message appears.

Or you can use markdown check boxes and write them up per feature:

**Manual Testing For Contact Form**
- [x] try to submit 
- [x] Try to submit the empty form and verify that an error message about the required fields appears
- [x] Try to submit the form with an invalid email address and verify that a relevant error message appears
- [x] Try to submit the form with all inputs valid and verify that a success message appears.
- [x] no console errors
- [x] submit goes to code institute data dump page in new tab
- [x] looks good on mobile (one column)
- [x] looks good on tablet (two columns)
- [x] looks good on desktop (two columns but not SUPER HUGE)

Or you can use a spreadsheet
    
Here is a [Manual Testing Template](https://docs.google.com/spreadsheets/d/1vc1IVL-ydQwWeWMqnk_GRox6HE6qxDLpchGse8Crayo/edit#gid=296578096) that you can use as a starting point to keep track of your testing efforts. Make a copy of it in your own account and update as needed to reflect the browsers you are testing and features.  

It's ok to spot check specific functionality across devices and browsers but each page should be viewed as a whole for each device/browser combo at least once.

A quick way to check if items are exceeding the screen width of a project is to run this javascript in the console for various screen emulations:

```
var docWidth = document.documentElement.offsetWidth;
[].forEach.call(document.querySelectorAll('*'),function(el){if(el.offsetWidth > docWidth){console.log(el);}});
```

## Compatibility and Responsive Testing
🚨**Required** 

>To save time, you can create this type of table in [markdown table generator](https://www.tablesgenerator.com/markdown_tables)
>
>As of Feb 14, 2022 CI students can take advantage of the Student Developer Pack where you have access to great things like [browserstack](https://education.github.com/pack/offers/#browserstack) You should have received an email about how to activate your student Developer Pack, here's a [slack](https://code-institute-room.slack.com/archives/C0L316Z96/p1644946870567999) with details if you can't find it in the associated thread.


Minimally you should use dev tools and emulators to try to test you site on various screen sizes and browsers and note it in a table:

I ensured my site was worked well, and looked nice on a variety of devices & browsers as noted in the table below:

| TOOL / Device                 | BROWSER     | OS         | SCREEN WIDTH  |
|-------------------------------|-------------|------------|---------------|
| real phone: motog6            | chrome 78   | android 8  | XS 360 x 640  |
| browser stack: iPhone5s       | safari  13  | iOs        | XS 320 x 568  |
| dev tools emulator: pixel 2   | firefox  69 | android 8  | SM 411 x 731  |
| browserstack: iPhone 10x      | Chrome 78   | iOs 11     | SM 375 x 812  |
| browserstack: nexus 7 - vert  | Chrome 78   | android 7  | M 600 x 960   |
| real tablet: ipad mini - vert | safari  13  | iOs 6      | M 768 x 1024  |
| browserstack: nexus 7 - horiz | firefox 69  | android 7  | LG 960 x 600  |
| chrome emulator: ipad - horiz | safari 13   | iOs        | LG 1024 x 768 |
| browserstack windows PC       | Chrome 78   | windows 10 | XL 1920 x 946 |
| real computer: mac book pro   | safari 12.1 | Mohave     | XL 1400 x 766 |
| browserstack windows pc       | IE Edge 88  | windows 10 | XL 1920 x 964 |


🚀 **merit & beyond**
Document why you chose the devices:

1. Visit https://gs.statcounter.com/browser-market-share to figure out the most popular browsers & operating system combos seen across the web for the geographic region, and platform(s) and screen sizes you expect your users to belong to. 

2. Include a sentence about why you chose the combinations you did.

3. Create a table that lists out what devices, browsers, and operating system you tested your application on and a brief description of why you chose the mixture you did. The point is to prove that you looked at the site across various browsers, operating systems, and viewport breakpoints.

4. if you can't find the browser/device/OS combinations you want on Browserstack with your GitHub student webpack (or you didn't activate that in time), note what you'd ideally test on then what you ended up testing on as a compromise. 

5. Build a table to summarize the choices you made [markdown table generator](https://www.tablesgenerator.com/markdown_tables)

The combinations above were chosen because of the following information I gathered  from [ga.statcounter.com]( https://gs.statcounter.com/browser-market-share) for the US from Aug-Oct 2021:
**browser Version Market Share**:
  - safari iphone: 26.32%
  - chrome for android: 21.32%
  - Chrome 105.0: 15.77%
  - Chrome 104.0: 6.28%
  - Edge 105: 4.99%
  - Safari 15.6 3.76%
**browser Market Share**
  - chrome: 50.28%
  - Safari: 34.65%
  - Edge: 6.37%
  - Firefox: 3.52%
  - Samsung Internet: 2.04%
  - Opera: 0.89%
**platform breakdown**
  - mobile: 51.26%
  - desktop: 45.73%
  - tablet: 2.97%
  - console: 0.03%

## Accessibility Testing
🚨**Required** 

Accessibility testing is aimed to make sure that those with visual or physical disabilities can still browse your website. Some users have had strokes or accidents that make it difficult to use a mouse, so they use keyboard keys to tab through sites. Others use screen readers that rely on HTML tags to help the user navigate quickly through the site to find information they want, others have color blindness or contrast issues. It's the law to provide services 
Here's a [site](https://www.w3.org/WAI/fundamentals/accessibility-intro/#:~:text=Accessibility%20is%20Important%20for%20Individuals%2C%20Businesses%2C%20Society,-The%20Web%20is&text=That%20is%2C%20the%20accessibility%20barriers,older%20people) where you can learn more about accessibility and the internet.

### Accessibility Audits
🚨**Required** 

Accessibility audits run through the HTML and determine if the parts of the WCAG (web content accessibility guidelines ) that are implemented through HTML tags and attributes are present. They can do some checking for low vision/contrast stuff too.

You should run your deployed website pages through  at least on auditing tool. lighthouse's audit to check performance, accessibility, best practices and SEO scores. You should aim to get 85 or higher score on accessibility. 

**You should fix issues associated with:**
- contrast 
- aria labels
- alt text
- large images
- skewed images

**Lighthouse**
https://web.dev/measure/  If you have lower scores, read the report and follow the links to address the flagged issues. You can run this tool from Chrome Dev Tools too against your local machine, but chrome extensions can sometimes give you missing alt text on things like the grammarly plug in tracking pixel.

You want a score in the green for accessibility and should look at ways to get it to 100.


**[WAVE chrome](https://chrome.google.com/webstore/detail/wave-evaluation-tool/jbbplnpkjmmeebjpijfedlgcdilocofh?hl=en-US) extension**
Wave is developed by webaim.org and does a bit better at contrast issues and uses 2.1 guidelines

**Contrast Checkers**
- https://webaim.org/resources/contrastchecker/
- https://color.a11y.com/

### Keyboard Navigation
Esports Teammates is optimized for keyboard navigation!

## Core Web Vitals
🚀 **merit & beyond**

SEO is greatly impacted by your core web vitals. The readout from https://web.dev/measure/ which is essentially a lighthouse audit gives your site scores in 4 categories. Ideally you want your site to be in the green for all 4 scores. web.dev has dedicated servers to test deployed sites without extensions that skew the results, so it's best to get results from this site.
 You should talk about the results for each section pay attention to 

## Validation Testing
### CSS Validation
The [Jigsaw validator](https://jigsaw.w3.org/css-validator/) was used to validate CSS.
No errors were found.

![image](https://github.com/PPindel/esports-teammates/assets/114284732/4700efa2-1821-44f0-9ec3-219209e85671)

### HTML Validation
The **[W3 HTML Validator](https://validator.w3.org/)** was used to validate HTML by coping the page source as a direct input.
No errors were found.

Landing page:

![image](https://github.com/PPindel/esports-teammates/assets/114284732/068dfa08-fcc7-4fde-8d80-fae7abe3c19a)

Signup page:

![image](https://github.com/PPindel/esports-teammates/assets/114284732/a1010812-5d6e-4aa2-a84a-e54ae28c5b1a)

Login page:

![image](https://github.com/PPindel/esports-teammates/assets/114284732/859d4764-485e-4e6e-8c25-c94707aec4a8)

Home page:

![image](https://github.com/PPindel/esports-teammates/assets/114284732/f824bb0c-b579-4091-8d89-f427f67375e3)

Team Detail page:

![image](https://github.com/PPindel/esports-teammates/assets/114284732/49ac477d-a53b-47d3-894b-8bfd35420d4d)

Add Team Ad page:

![image](https://github.com/PPindel/esports-teammates/assets/114284732/d0e4cdc0-59d1-4bd6-b07e-55d6c2770f07)

Sign out page:

![image](https://github.com/PPindel/esports-teammates/assets/114284732/97f7e5ed-a91e-4e3f-b297-d3474c89168b)

Edit Team Ad page:

![image](https://github.com/PPindel/esports-teammates/assets/114284732/7429242d-a9d3-4a3c-bbd1-eb9f4e0b10f9)

Delete Team Ad page:

![image](https://github.com/PPindel/esports-teammates/assets/114284732/ae031252-c0e9-482f-a1cf-e6c1589c9db6)

Edit comment page:

![image](https://github.com/PPindel/esports-teammates/assets/114284732/2e6e214c-650a-4802-9f6a-d9258a51e89a)

404 error page:

![image](https://github.com/PPindel/esports-teammates/assets/114284732/47305e86-41f4-4bf5-abcf-ed75ecd0e32a)

### JavaScript Validation
The **[Jshint validator](https://jshint.com)** was used to validate the JS function.
No errors were found.

![image](https://github.com/PPindel/esports-teammates/assets/114284732/5b02c45b-428f-4f8a-b204-4e224443ba9f)

### Python Validation
**[CI's pep8 tool](https://pep8ci.herokuapp.com/)** was used to validate each .py file created.
No errors were found.

In Blog folder:
admin.py:

![image](https://github.com/PPindel/esports-teammates/assets/114284732/0f96eabe-e1c3-4683-9010-00145026a624)

apps.py:

![image](https://github.com/PPindel/esports-teammates/assets/114284732/e549cfd6-bfe7-4c42-a390-1523579e7db7)

forms.py:

![image](https://github.com/PPindel/esports-teammates/assets/114284732/cb067742-55c6-4099-ae00-685f7a43b4f8)

models.py:

![image](https://github.com/PPindel/esports-teammates/assets/114284732/e94fc459-d7d2-4475-870f-08768aac46d1)

urls.py:

![image](https://github.com/PPindel/esports-teammates/assets/114284732/f31620f9-39e4-437e-9ae9-dee39ddcba3b)

views.py:

![image](https://github.com/PPindel/esports-teammates/assets/114284732/f09d16da-35ff-4d20-a84b-8d0b76776c64)

In teamfinder folder:
asgi.py:

![image](https://github.com/PPindel/esports-teammates/assets/114284732/e322521c-b17e-4a2b-9769-2e8f2b58a4e9)

settings.py:

![image](https://github.com/PPindel/esports-teammates/assets/114284732/0cffe5e8-7e2f-454e-8f6b-01276bd7e2a6)

urls.py:

![image](https://github.com/PPindel/esports-teammates/assets/114284732/bbf374c9-7d6a-4c44-80e0-3f0b85b80f44)

util.py:

![image](https://github.com/PPindel/esports-teammates/assets/114284732/75e90b6a-2178-495e-b369-322e7928bfa3)

wsgi.py:

![image](https://github.com/PPindel/esports-teammates/assets/114284732/4687d15d-375d-47b6-a7fe-f7be66f89c2e)

In main folder:
manage.py:

![image](https://github.com/PPindel/esports-teammates/assets/114284732/cd2f8062-c6c1-4495-92a5-6a04f47d6be9)

# Defects
🚨**Required** 

At this point you need to be using GITHUB's Issues to track these as it helps you with the AGILE process requirement and it's really easy to copy/paste screenshots in and then write up how you closed them.

[Here's a brief overview](https://docs.google.com/document/d/1nDS5tZeMO77Dfq85IZGMSV6C41XaPm9FwcpR3k-UTVc/edit#heading=h.542xzc8ufx4x) I put together on how to do this.

This what my custom bug template looks like in the UX
![image](https://user-images.githubusercontent.com/23039742/165650359-a352d64e-b128-473d-ab60-7df0568a44df.png)

- provide a link to the issues link in GitHub
- if you made a custom template include a screenshot
- if you made a custom template include a link to the template

## Defects of Note
🚀 **merit & beyond**

Some defects are more pesky than others. Highlight 3-5 of the bugs that drove you the most nuts and link to them directly here. The accessors really like to know the struggle is real and that by doing this you picked up more skills.

## Outstanding Defects
🚨**Required** 

It's ok to not resolve all the defects you found as long as:
- it does not impact a user from completing a vital function on the website
- it only affects a very small subset of users
- is an extreme edge case that very few users would try
- there is an open issue against a framework, browser or technology used

If you know of something that isn't quite right, create an issue and link to it here and explain why you chose not to resolve it. 

Sometimes it's as simple, word wrapping issue that makes the site look odd at a certain screensize that you just didn't have time to fix due to the impending deadline it's best to mention it but note why you allowed it to go live: "Yes it looks odd, but it doesn't impact core functionality of the site." than to let the accessors think you didn't notice it. 

# Technologies Used
## Languages
- html
- css
- java script
- python
- django

## Frameworks, Libraries & Programs Used
- Balsamiq
- Coolors.co
- fontawesome
- pexels.com
- gitpod
- github
- google fonts
- https://techsini.com/multi-mockup/index.php - responsiveness
- table of contents creator
- markdown table generator
- Heroku
- Cloudinary
- ElephantSQL
- Bootstrap

# Deployment 
## Fork and Clone the Repository
To keep the main reposotory for this project clean, please fork the repostiory into your own account. GitHub has [forking directions](https://docs.github.com/en/get-started/quickstart/fork-a-repo#forking-a-repository) but here's what you might do:
1. login to your own gitHub account
2. navigate to [my repository](https://github.com/PPindel/esports-teammates)
3. In the top right corner of the page, click fork 

![image](https://user-images.githubusercontent.com/23039742/213840378-e785eaa0-712b-468c-bcda-64fde56eae44.png)

4. set yourself as the owner
5. change the name of the repo if you want
6. add a description if you want
7. choose what to copy, typicall the main branch only
8. click the snazy green button

![image](https://user-images.githubusercontent.com/23039742/213840549-5bef12ae-198e-412b-84b6-0cc718b6fa1d.png)

9. To get files to your local environment, you need to clone it: click the code button
10. Copy the url as needed (here's gitHub instructions)[https://docs.github.com/en/get-started/quickstart/fork-a-repo#cloning-your-forked-repository}

## Development Deployment
- Install required python packages: `pip3 install -r requirements.txt`
- Create env.py
- In env.py:
>  - os.environ["SECRET_KEY"] = "<YOUR_VALUE>"
>  - os.environ["CLOUDINARY_URL"] = "<YOUR_VALUE>"
>  - os.environ["DATABASE_URL"] = "<YOUR_VALUE>"
- Apply Database Migrations so the database starts up `python3 manage.py migrate`
- Create a super user so you can add and inspect things via django admin  `python3 manage.py createsuperuser`
- Start the server `python3 manage.py runserver`

## Production Deployment
- create new Heroku app

![image](https://github.com/PPindel/esports-teammates/assets/114284732/3f4174b5-8e47-445b-a66a-207e2fe84fc6)

- set app name and select your region

![image](https://github.com/PPindel/esports-teammates/assets/114284732/19841c4c-3ad8-47a1-ab01-310e5d9aaedb)

- login to ElephantSQL, access the dashboard and create a new instance (input a name, select a region), then return to dashboard, copy the database URL

![image](https://github.com/PPindel/esports-teammates/assets/114284732/3a9ac5d3-14bb-4ef3-87b7-62bcc398fbce)

- login to Cloudinary, access the dashbord and copy your API key

![image](https://github.com/PPindel/esports-teammates/assets/114284732/c1069f1a-9bdb-41e4-bb35-ad0bc7c6e14f)

- add environmental values (some of variables are identical as in your env.py file)
>  - SECRET_KEY
>  - CLOUDINARY_URL
>  - DATABASE_URL
>  - COLLECT_STATIC
>  - Port

![image](https://github.com/PPindel/esports-teammates/assets/114284732/a5fa519b-827e-4377-9729-7717880564d5)

- add build packages

![image](https://github.com/PPindel/esports-teammates/assets/114284732/101d23b5-f300-42a1-abe1-83737b695627)

- connect to github

![image](https://github.com/PPindel/esports-teammates/assets/114284732/9c005f23-ef9b-4e6d-aefa-f559254d291e)

- deploy! (remember to watch monitor logs for any deployment issues)

![image](https://github.com/PPindel/esports-teammates/assets/114284732/07141992-6ee6-48b5-8332-4b9d7a81c63b)

# Credits

- https://www.geeksforgeeks.org/ - code solutions
- https://stackoverflow.com/ - code solutions
- https://www.w3schools.com/ - code solutions
- https://learndjango.com - code solutions
- https://github.com/CaraMcAvinchey/stem-and-leaf-blog - some code inspirations
- https://www.youtube.com/@Codemycom - Create A Simple Django Blog by John Elder
- https://github.com/Code-Institute-Org/gitpod-full-template - Code Institute Template

## Media

- https://pexels.com
- (users can add their own pictures to Team Ads, so I cannot point the source of all images...)

## Acknowledgments

Big thanks to Malia Havlicek - Code Institute mentor for her ideas and support in this project! Also, I would like to thank all my friends for live testing the program!

https://pep8ci.herokuapp.com/ - code validation tool
