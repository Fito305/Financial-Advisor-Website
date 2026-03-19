# AGENT.md

## Role
You are an expert web developer and UI/UX designer building a professional single-page application for a financial advising business.

## Objective
Create a polished, modern, minimal **single-page application** with section scrolling on one page.

The business owner will later edit the final wording and images, so all business copy should be clearly written as easy-to-replace placeholder text.

## Tech Stack
Use the following stack:

- **Frontend:** plain HTML, CSS, vanilla JavaScript
- **Backend:** Python with FastAPI
- **Templating:** Jinja templates are allowed and should be used where helpful
- **Database:** SQLite
- **Layout approach:** grid-based CSS section layouts

Do not use frontend frameworks such as React, Vue, Angular, or similar.

## Site Type
Build a **true client-side SPA-style single-page website** with:

- one main page
- a sticky navigation bar
- smooth scrolling between sections
- section-based navigation
- responsive layout for desktop, tablet, and mobile

## Visual Design Direction
The website should feel:

- modern
- minimal
- professional
- trustworthy
- clean
- conversion-focused

## Color Direction
Use an **orange and black** theme.

Design expectations:

- black or near-black primary backgrounds
- orange used as the primary accent color
- strong readability and contrast
- modern and minimal aesthetic
- avoid clutter
- avoid flashy effects
- avoid overly corporate blue-bank style visuals

## Core Sections
The page must include the following sections in this order unless a better layout improves UX:

### 1. Sticky Navbar
Include:

- brand / logo placeholder
- nav links that scroll to page sections
- CTA-style nav item if appropriate
- mobile-friendly navigation behavior

Suggested links:

- Financial Adviser
- About Me
- Testimonials
- Investment Specialty
- Contact

### 2. Financial Adviser Section
This is the **hero / landing section** at the top of the page.

Include:

- main headline placeholder
- supporting subheadline placeholder
- short professional summary placeholder
- primary CTA button placeholder
- secondary CTA button placeholder if helpful
- optional image / portrait placeholder
- strong first impression focused on trust and professionalism

### 3. About Me Section
Include:

- advisor bio placeholder
- mission / philosophy placeholder
- image placeholder
- supporting cards or bullet points with placeholder text
- layout that supports professionalism and trust

### 4. Testimonials Section
Use **hardcoded placeholder testimonial cards** for now.

Requirements:

- use clearly fake placeholder text that is easy to replace
- include placeholder client name fields
- include placeholder client title or relationship fields
- do not fabricate real people
- do not imply testimonials are real
- style cards cleanly and professionally

### 5. Investment Specialty Section
Include placeholder content for specialties or focus areas.

Examples of structure only:
- retirement planning
- investment guidance
- wealth strategy
- portfolio planning
- risk management

These are only structural placeholders and must be easy to replace later.

Use a clean grid layout for specialty cards or panels.

### 6. Call to Action Section
This section must include:

- short CTA headline placeholder
- supporting text placeholder
- contact form
- Calendly scheduling link placeholder

The form should collect:

- name
- email
- phone number

The Calendly option should be a simple `<a>` element placeholder that the owner can later replace with a real Calendly URL.

## Backend Requirements
Build a FastAPI backend that supports the frontend.

### Form Submission Requirements
The contact form must:

- submit to the FastAPI backend
- validate required fields
- store submissions in a database
- send an email notification when a submission is received

### Database
Use **SQLite** for storage.

Requirements:

- keep setup simple
- store contact form submissions in SQLite
- use a clean, understandable schema
- make database usage straightforward for a small business site

### Email Notification
Implement backend logic for email notification after a successful form submission.

Requirements:

- use environment variables or configuration placeholders for email settings
- keep credentials out of source code
- make the email notification flow easy to configure later
- do not hardcode real credentials
- use placeholders where needed

## Content Rules
All content must be placeholder content unless it is purely structural UI text.

Use obvious placeholder patterns such as:

- `[Business Name]`
- `[Hero Headline Placeholder]`
- `[Short Advisor Bio Placeholder]`
- `[Testimonial Placeholder]`
- `[Calendly Link Placeholder]`
- `[Phone Number]`
- `[Email Address]`

Do not invent:

- real testimonials
- real credentials
- real certifications
- real office addresses
- real performance claims
- real guarantees
- fake compliance disclosures presented as real

## UX Requirements
The website should guide the visitor toward trust and action.

Priorities:

- clear navigation
- easy section scanning
- strong hierarchy
- clean spacing
- simple interaction
- obvious next step
- mobile usability
- accessible form labels and inputs

## CSS / Layout Requirements
Use clean, maintainable CSS.

Requirements:

- grid-based layout per section where appropriate
- responsive breakpoints
- reusable utility or section patterns if helpful
- consistent spacing system
- clear typography hierarchy
- visually balanced orange accent usage
- strong button styling
- polished card layouts
- smooth scrolling behavior

## JavaScript Requirements
Use vanilla JavaScript only.

Use JavaScript for things like:

- navbar mobile toggle behavior
- smooth scroll enhancements if needed
- form submission handling if appropriate
- small UI interactions only

Do not overengineer the JavaScript.

## Jinja Requirements
Use Jinja where helpful to keep templates clean and maintainable.

Examples of acceptable use:

- template inheritance if helpful
- reusable partials
- injecting placeholder values or configuration
- separating layout cleanly

Keep the project simple and easy to edit.

## Project Structure
Generate a complete project structure for this website.

Include at minimum:

- FastAPI app entry point
- templates directory
- static CSS directory
- static JavaScript directory
- database-related setup
- form handling backend logic
- email notification integration structure
- environment/config placeholders
- clean folder organization

## Editing Expectations
The owner should be able to easily edit later:

- hero text
- about me text
- specialty text
- testimonials
- Calendly link
- contact details
- branding assets
- colors if needed

Keep placeholder content easy to find and replace.

## Do Not
Do not:

- use React or any JS framework
- use fake real-world business claims
- use fake client reviews presented as real
- create unnecessary complexity
- bury editable text in difficult locations
- make the design noisy or flashy
- prioritize animation over clarity
- add unnecessary pages beyond what is needed for this one-page site

## Success Criteria
The result should be a professional, modern, orange-and-black financial advising SPA that includes:

- a sticky navbar
- one-page section scrolling
- hero-style Financial Adviser section
- About Me section
- hardcoded placeholder Testimonials section
- Investment Specialty section
- CTA section with form and Calendly link placeholder
- FastAPI backend
- SQLite storage
- email notification support
- plain HTML + Jinja + vanilla JS + CSS
- clean grid-based responsive layout

The final result should look polished and real, while keeping all business text and details clearly editable as placeholders.
