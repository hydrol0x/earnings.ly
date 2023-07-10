ten_k_items = {
    "Business": "1",
    "Risk Factors": "1A",
    "Unresolved Staff Comments": "1B",
    "Properties": "2",
    "Legal Proceedings": "3",
    "Mine Safety Disclosures": "4",
    "Market for Registrant’s Common Equity, Related Stockholder Matters and Issuer Purchases of Equity Securities": "5",
    "Selected Financial Data": "6",
    "Management’s Discussion and Analysis of Financial Condition and Results of Operations": "7",
    "Quantitative and Qualitative Disclosures about Market Risk": "7A",
    "Financial Statements and Supplementary Data": "8",
    "Changes in and Disagreements with Accountants on Accounting and Financial Disclosure": "9",
    "Controls and Procedures": "9A",
    "Other Information": "9B",
    "Directors, Executive Officers and Corporate Governance": "10",
    "Executive Compensation": "11",
    "Security Ownership of Certain Beneficial Owners and Management and Related Stockholder Matters": "12",
    "Certain Relationships and Related Transactions, and Director Independence": "13",
    "Principal Accountant Fees and Services": "14",
    "Exhibits, Financial Statement Schedules": "15"
}

ten_q_items = {
    "Financial Statements": "part1item1",
    "Management’s Discussion and Analysis of Financial Condition and Results of Operations": "part1item2",
    "Quantitative and Qualitative Disclosures About Market Risk": "part1item3",
    "Controls and Procedures": "part1item4",
    "Legal Proceedings": "part2item1",
    "Risk Factors": "part2item1a",
    "Unregistered Sales of Equity Securities and Use of Proceeds": "part2item2",
    "Defaults Upon Senior Securities": "part2item3",
    "Mine Safety Disclosures": "part2item4",
    "Other Information": "part2item5",
    "Exhibits": "part2item6"
}

eight_k_items = {
    "Entry into a Material Definitive Agreement": "1-1",
    "Termination of a Material Definitive Agreement": "1-2",
    "Bankruptcy or Receivership": "1-3",
    "Mine Safety - Reporting of Shutdowns and Patterns of Violations": "1-4",
    "Completion of Acquisition or Disposition of Assets": "2-1",
    "Results of Operations and Financial Condition": "2-2",
    "Creation of a Direct Financial Obligation or an Obligation under an Off-Balance Sheet Arrangement of a Registrant": "2-3",
    "Triggering Events That Accelerate or Increase a Direct Financial Obligation or an Obligation under an Off-Balance Sheet Arrangement": "2-4",
    "Cost Associated with Exit or Disposal Activities": "2-5",
    "Material Impairments": "2-6",
    "Notice of Delisting or Failure to Satisfy a Continued Listing Rule or Standard; Transfer of Listing": "3-1",
    "Unregistered Sales of Equity Securities": "3-2",
    "Material Modifications to Rights of Security Holders": "3-3",
    "Changes in Registrant\"s Certifying Accountant": "4-1",
    "Non-Reliance on Previously Issued Financial Statements or a Related Audit Report or Completed Interim Review": "4-2",
    "Changes in Control of Registrant": "5-1",
    "Departure of Directors or Certain Officers; Election of Directors; Appointment of Certain Officers: Compensatory Arrangements of Certain Officers": "5-2",
    "Amendments to Articles of Incorporation or Bylaws; Change in Fiscal Year": "5-3",
    "Temporary Suspension of Trading Under Registrant\"s Employee Benefit Plans": "5-4",
    "Amendments to the Registrant\"s Code of Ethics, or Waiver of a Provision of the Code of Ethics": "5-5",
    "Change in Shell Company Status": "5-6",
    "Submission of Matters to a Vote of Security Holders": "5-7",
    "Shareholder Nominations Pursuant to Exchange Act Rule 14a-11": "5-8",
    "ABS Informational and Computational Material": "6-1",
    "Change of Servicer or Trustee": "6-2",
    "Change in Credit Enhancement or Other External Support": "6-3",
    "Failure to Make a Required Distribution": "6-4",
    "Securities Act Updating Disclosure": "6-5",
    "Static Pool": "6-6",
    "Alternative Filings of Asset-Backed Issuers": "6-10",
    "Regulation FD Disclosure": "7-1",
    "Other Events": "8-1",
    "Financial Statements and Exhibits": "9-1",
    "Signature": "signature"
}



company_info_prompt = """
User: What"s new with Dropbox"s cloud storage technology?

PALM:
{"companyName": "Dropbox","Form": "8-K","Section": "Recent Developments"}

User: How did Chipotle perform in their latest quarterly earnings?

PALM:
{"companyName": "Chipotle","Form": "10-Q","Section": "Financial Highlights"}

User: Any risks that GoPro mentioned in their recent annual report?

PALM:
{"companyName": "GoPro","Form": "10-K","Section": "Risk Factors"}

User: What kind of payout did the executives at Etsy get according to their recent filing?

PALM:
{"companyName": "Etsy","Form": "10-K","Section": "Executive Compensation"}

User: What"s new in Starbucks" world?

PALM:
{"companyName": "Starbucks","Form": "8-K","Section": "Recent Developments"}

User: How are Caterpillar"s finances looking from their last quarterly report?

PALM:
{"companyName": "Caterpillar","Form": "10-Q","Section": "Financial Highlights"}

User: Has Pfizer mentioned any concerns in their annual report?

PALM:
{"companyName": "Pfizer","Form": "10-K","Section": "Risk Factors"}

User: What"s the recent executive compensation scenario at JPMorgan Chase according to the filings?

PALM:
{"companyName": "JPMorgan Chase","Form": "10-K","Section": "Executive Compensation"}

User: Any updates on Roku"s future strategies from their latest filings?

PALM:
{"companyName": "Roku","Form": "10-K","Section": "Business Strategy"}

PALM:
{"companyName": "Berkshire Hathaway","Form": "10-Q","Section": "Market Risk Disclosures"}

User: Do you have any news on Zillow"s recent acquisitions?

PALM:
{"companyName": "Zillow","Form": "8-K","Section": "Acquisition News"}

User: Could you give me a run-down of Adobe"s operational and financial highlights from their last annual report?

PALM:
{"companyName": "Adobe","Form": "10-K","Section": "Operating and Financial Review"}
"""