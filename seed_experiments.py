from experiments import Experiments
from model import Model

seed = """
        Your job is to generate prompts that will generate prompts for a powerful LLM AI system. Here is a starting prompt dilineated by triple brackets that you can use to iterate and improve upon:

        [[[
            Your job is to generate human and system prompts for GPT-4, given the following starting prompt to iterate on and try to improve on here: 

            '''
            'System:',
                'As a Cover Genius insurance content writer and editor, your task is to generate engaging and informative content for insurance policies. You will be provided with insurance briefs for specific insurance
                products. Your goal is to create compelling insurance policy content using simple language that is easy to understand. The provided briefs have sections with headings that you can use as templates for 
                your content. Use bullet points to list the conditions under which someone is protected or not protected by the insurance policy. Additionally, include a section on how claims work, also using bullet 
                points. Remember to review the approved content library for similar sections that can be used as-is. Your content should be accurate, consistent, error-free, and align with the brand voice and tone of 
                Cover Genius. Let's begin generating the insurance policy content, section by section.',

            'Human:',
                'I have an interesting task for you as a Cover Genius insurance content writer and editor. Your role is to create compelling and informative content for insurance policies. You will receive briefs for 
                specific insurance products, and your goal is to generate engaging content using simple language. The briefs provide sections with headings that can serve as templates for your content. Make sure to 
                include bullet points for the conditions under which someone is protected or not protected by the insurance policy. Additionally, include a section on how claims work, also using bullet points. Remember 
                to check the approved content library for any existing sections that can be incorporated. It is important to create accurate, consistent, and error-free content that reflects the brand voice and tone of 
                Cover Genius. Let\'s get started and generate the insurance policy content, section by section.'
            '''

            The prompts you will be generating will be for generating content for Cover Genius insurance policies based on a content brief provided by an insurance team. 
            Your prompts will be ranked on the quality of the outputs on coherence, relevance, consistency, fluency, informativeness, naturalness, and use of simple language, so try and maximize these qualities in the outputs of your prompts.
            Do not tailor the prompt to a specific insurance vertical, make it general purpose for any insurance policy, but the content that is generated should be a specific insurance policy.
            In your generated prompt, you should describe how the AI should behave in plain English. Include what it will see, and what it's allowed to output. 
            Be creative with prompts to get the best possible results. The AI knows it's an AI -- you don't need to tell it this.
            You will be graded based on the performance of your prompt... but don't cheat! You cannot include specifics about the briefs in your prompt. Any prompts with examples will be disqualified.
            Most importantly, output NOTHING but the prompt. Do not include anything else in your message.
        ]]]

        The prompts you will be generating will be for generating prompts for Cover Genius insurance policies based on a content brief provided by an insurance team.
    """

booking_protect_brief = """
Booking Refund Protection
All refunds are administered by XCover.com. You will be provided with a refund on any unused booking if you are unable to attend the booked event due to any of the circumstances set out below. 
Definitions
The following words or phrases have the meaning shown below wherever they appear in bold in this document.
You/Your/Yourself – A person who has made a booking alone or as part of a group with us.
Doctor – A qualified medical practitioner registered with a recognised professional body. A doctor cannot be you or a member of your immediate family.
Emergency Services – The Police, Fire and Rescue Service or Emergency Medical Services.
Booking/Booked event – The pre-planned and pre-booked service(s)/event(s)/ticket(s) including booking and service fees transacted with us by you.
Group – Any number of people who have made a booking with us with Booking Refund Protection in the same transaction.
Illness – A physical or mental condition confirmed by a doctor that prevents you from attending the booked event.
Immediate family – Your husband, wife, partner, civil partner, parent, child, brother or sister.
Injury - A bodily injury confirmed by a doctor that prevents you from attending the booked event.
Public Transport Network – Any mode of public transport other than public hire taxis licensed for public use on which you had planned to travel to a booked event.
Ticket – A non-refundable, authorised ticket that was purchased from us where Booking Refund Protection has also been purchased at the same time as purchasing the Ticket(s).
We/us/our – The booking vendor with whom you made the booking. Go to xcover.com/claim to start your claim.
What will we refund?
We will refund the cost of your booking if you are unable to attend a booked event due to:
unexpected disruption of the public transport network you could not have reasonably known about before the date of the booked event;
an injury, or an illness affecting you or a member of your immediate family;
death happening to you at anytime before the booked event or a member of your immediate family within a 4 week period of the booked event;
the mechanical breakdown, accident, fire or theft en route of a private vehicle taking you to the booked event;
jury service which you were unaware of at the time of the purchase;
burglary or fire at your residence in the 48 hours immediately before the booked event that required the attendance of the emergency services;
you being summoned to appear at court proceedings as a witness which you were unaware of at the time of purchase;
you being a member of the armed forces and being posted overseas unexpectedly;
adverse weather including snow, frost, fog or storm where the Police services or other Government agencies have issued warnings not to travel. You must provide confirmation of relevant road closures from the Police or the relevant Government agency;
you are being relocated permanently for work by your employer more than 100 miles from the booked event which you were unaware of at the time of booking or you are unexpectedly made compulsory redundant.
What will we not refund?
We will not provide a refund where:
you cannot provide a doctor’s report for injury or illness;
you cannot return all unused tickets or vouchers forming part of the booking;
your sole reason for not attending is due to another member of your group no longer being able to attend for any reason;
you are unable to attend a booked event because you are unable to obtain a visa to travel;
the booked event is cancelled, abandoned, postponed, curtailed or relocated;
you decide not to attend a booked event other than for a reason included within this Booking Refund Protection;
you are prevented from travelling to a booked event due to disruption of the public transport network which is public knowledge prior to the booked event;
you are being relocated temporarily for work by your employer at the time of booking or you have applied for relocation more than 100 miles from the booked event;
you can recover any part of the booking;
In our reasonable opinion, you did not allow sufficient time to travel to a booked event;
you carry out a criminal act which prevents you attending a booked event;
you are prevented from travelling to a booked event due to an outbreak of a contagious disease and the Government or any agency acting on behalf of the Government has imposed a ban on travel;
you make a false or fraudulent refund application or support a refund application by false or fraudulent document, device or statement;
you submit your refund request more than 45 days after the booked event.

We will not pay for travelling or associated expenses (unless travel costs are included as part of the total package price), or any loss other than the purchase price, of the booked event.
We will not pay any consequence of war, invasion, acts of foreign enemies, hostilities (whether war be declared or not), civil war, rebellion, revolutions, insurrection, military or usurped power, riot, civil commotion, strikes, lockout, terrorism, malicious intent or vandalism, confiscation or nationalisation of or requisition or destruction of or damage to property by or under the order of any government or public or local authority. 
We will not pay any costs you incur in submitting or providing evidence to support your refund application.
General Conditions 
You must make all necessary arrangements to arrive on time. 
You must not be aware of any material fact, matter or circumstance, at the time Refund Protection is purchased, which may give rise to a refund request. 
You must take all reasonable precautions to prevent or reduce any request for a refund. 
Unless we agree otherwise: 
the language of this document and all communications relating to it will be English; and 
all aspects of the contract, including negotiation and performance, are subject to English laws and the decisions of English courts. 
Booking Refund Protection is non-refundable unless cancelled within 14 days of purchase and the booked event has not taken place. To cancel the refund protection you need to contact the vendor within 14 days.
Requesting a Refund 
Go to xcover.com/claim to start your claim. Our claims team prioritises those claims that are filed within 7 days of the claim event.
Provide a detailed description of the event.
For all claims we require, as a minimum, a detailed description of the event. We may request further information during the claim process such as booking invoices and receipts. If required documents are not provided to us the claim may be rejected or the status changed to “Pending”.
You will be asked to provide at your own expense the following within 45 days of registering your refund application: 
the original unused tickets for all parts of the booking; 
a doctor’s report where your refund request is for injury or illness or a death certificate where your refund request is for death; 
an official notice from the transport service provider in the event of delay, cancellation, mechanical breakdown or accident in relation to the public transport network; 
for the breakdown of a private vehicle, a vehicle recovery service report (AA, RAC or equivalent), copy of garage repair bill or parts receipt or in the case of vehicle repairers or police;
the original jury invitation inviting you to be a juror; 
in the event of a burglary the police report with crime reference number; 
the original witness summons requesting you to appear in court; 
a copy of a valid visa permitting your travel to the booked event; 
confirmation of relevant road closures from the Police or the relevant Government agency if requesting a refund due to an official weather warning being issued;
any reasonable additional evidence that we ask for."""


coverage = """
You're not covered if...
Customer makes a mistake when making their booking and can't go on their trip.
Customer can't travel due to work or school commitments.
Customer can't travel due to work commitments.
The event customer was travelling to is cancelled or rescheduled.
Due to changes in personal circumstances.
Failure to provide all the required travel documents (eg passport, visa).
Customer can't travel due to financial reasons. 
"""

trip_cancellation = """
HOW DOES IT WORK?    

THIS PROTECTS YOUR PRE-PAID TRAVEL/FLIGHT EXPENSES IF YOU HAVE TO CANCEL OR CUT SHORT YOUR TRIP. 
XCover.com’s Trip Cancellation Protection is sold by our partner {{partner.subsidiary.title}}. It includes protection for your pre-paid travel expenses, including flights and accommodations, if you have to cancel your trip. This includes pre-existing medical conditions and Covid-19 related cancellations. 

Prepaid cruises/cruise activities are not covered.

Your protection starts immediately after purchase. The following is a high-level summary.
SUMMARY OF YOUR PROTECTION    
YOU’RE PROTECTED IF… 
You have to cancel, interrupt or cut short your trip because you or a close relative become ill or are injured. This includes pre-exisiting medical conditions and Covid-19 related cancellations.

The protection includes the following benefits and limits…
"""

tests = [booking_protect_brief, coverage, trip_cancellation]

ranking = """
    Your job is to rank the quality of two outputs generated by different prompts. The prompts are used to generate AI application ideas for a business.
    Rank the quality of the outputs on coherence, relevance, consistency, impact, fluency, informativeness, naturalness, and use of simple language.
    Think like a customer and what you would want to see when you were buying insurance, so it would be presented in a super digestible way, easy to read, easy to understand, simple, and beneficial.
    You will be provided with the task description, the test prompt, and two generations - one for each system prompt.
    Rank the generations in order of quality. If Generation A is better, respond with 'A'. If Generation B is better, respond with 'B'.
    Remember, to be considered 'better', a generation must not just be good, it must be noticeably superior to the other.
    Also, keep in mind that you are a very harsh critic. Only rank a generation as better if it truly impresses you more than the other.
    Respond with your ranking, and nothing else. Be fair and unbiased in your judgement.
"""

model = Model('gpt-3.5-turbo-16k')

def main():
    name = "Ghostwriter Experiment 1"
    exp = Experiments(name, seed, tests, ranking, model)
    exp.save_to_file()

if __name__ == '__main__': main()