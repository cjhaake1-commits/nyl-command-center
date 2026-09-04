from __future__ import annotations

# Public/professional Simi Valley-area business prospects verified 2026-09-04.
BUSINESS_ROWS = [
    ('HLW Tax and Financial Services', 'Simi Valley', 'Accounting & Tax', '805-520-3300', 'https://hlwtax.com/', 'https://www.simivalleychamber.org/uploads/1/2/0/9/120906704/2025-2026_fall_winter_ssa_guide.pdf', 91),
    ('Michael P. Fischer, CPA, CITP', 'Simi Valley', 'CPA / Accounting', '805-522-3771', 'https://www.fischercpa.com', 'https://www.simivalleychamber.org/uploads/1/2/0/9/120906704/2025-2026_fall_winter_ssa_guide.pdf', 92),
    ('Paul Goodnough, CPA', 'Simi Valley', 'CPA / Accounting', '805-577-0526', 'https://www.countryclubcpa.com', 'https://www.simivalleychamber.org/uploads/1/2/0/9/120906704/2025-2026_fall_winter_ssa_guide.pdf', 92),
    ('Professional Business/Tax Services Inc.', 'Simi Valley', 'Accounting & Tax', '805-522-7763', 'https://thetaxbeacon.com', 'https://www.simivalleychamber.org/uploads/1/2/0/9/120906704/2025-2026_fall_winter_ssa_guide.pdf', 91),
    ('Skidmore Markell & Company, CPAs', 'Simi Valley', 'CPA / Accounting', '805-527-4024', 'https://www.skid-mark.com', 'https://www.simivalleychamber.org/uploads/1/2/0/9/120906704/2025-2026_fall_winter_ssa_guide.pdf', 92),
    ('Tony Tax & Notary Service', 'Simi Valley', 'Tax & Notary', '805-796-0974', 'http://www.tonytaxandnotaryservice.com/', 'https://www.simivalleychamber.org/uploads/1/2/0/9/120906704/2025-2026_fall_winter_ssa_guide.pdf', 86),
    ('Dallara Law', 'Simi Valley', 'Law Firm', '805-297-4510', 'https://dallaralaw.com', 'https://www.simivalleychamber.org/uploads/1/2/0/9/120906704/2025-2026_fall_winter_ssa_guide.pdf', 91),
    ('Erica Wise Law', 'Simi Valley', 'Law Firm', '805-376-1000', 'http://www.ericawiselaw.com/', 'https://www.simivalleychamber.org/uploads/1/2/0/9/120906704/2025-2026_fall_winter_ssa_guide.pdf', 90),
    ('Kevin L. Dorhout, Attorney at Law, APC', 'Westlake Village', 'Law Firm', '805-206-8977', 'https://dorhoutlaw.com', 'https://www.simivalleychamber.org/uploads/1/2/0/9/120906704/2025-2026_fall_winter_ssa_guide.pdf', 90),
    ('Law Firm of Artin Sodaify', 'Agoura Hills', 'Law Firm', '310-957-2442', 'http://www.artinsodaify.com/', 'https://www.simivalleychamber.org/uploads/1/2/0/9/120906704/2025-2026_fall_winter_ssa_guide.pdf', 88),
    ('Law Offices of Jennifer Monroe', 'Simi Valley', 'Estate Planning Law', '805-915-4760', 'https://trustyourway.com', 'https://www.simivalleychamber.org/uploads/1/2/0/9/120906704/2025-2026_fall_winter_ssa_guide.pdf', 93),
    ('Law Offices of Shantel J. Kuntuzos', 'Simi Valley', 'Law Firm', '805-496-1588', 'https://kuntuzoslaw.com', 'https://www.simivalleychamber.org/uploads/1/2/0/9/120906704/2025-2026_fall_winter_ssa_guide.pdf', 90),
    ('Attorney at Law / Alfred Keep', 'Simi Valley', 'Law Firm', '805-526-6221', 'https://alkeeplaw.com', 'https://www.simivalleychamber.org/uploads/1/2/0/9/120906704/2025-2026_fall_winter_ssa_guide.pdf', 88),
    ('Legal Production Service, Inc.', 'Simi Valley', 'Legal Services', '805-581-9192', 'https://lpstrust.com', 'https://www.simivalleychamber.org/uploads/1/2/0/9/120906704/2025-2026_fall_winter_ssa_guide.pdf', 87),
    ('Boregyde, Inc.', 'Simi Valley', 'Manufacturing', '805-583-5300', '', 'https://simivalleychambercacoc.wliinc1.com/Manufacturing', 86),
    ('Chatsworth Products', 'Simi Valley', 'Manufacturing', '818-734-3400', '', 'https://simivalleychambercacoc.wliinc1.com/Manufacturing', 84),
    ('Automated Manufacturing', 'Simi Valley', 'Manufacturing / Automation', '818-335-7070', 'https://www.automatedmfg.com/', 'https://www.automatedmfg.com/contact_us.html', 88),
    ('Forest Accounting and Tax', 'Simi Valley', 'Accounting & Tax', '805-915-4730', 'https://www.forestaccountingandtax.com/', 'https://www.forestaccountingandtax.com/contact.php', 90),
    ('Advanced Dental Implants USA', 'Simi Valley', 'Dental / Oral Surgery', '805-522-4022', 'https://advanceddentalimplantsusa.com', 'https://local.yahoo.com/info-228168287-advanced-dental-implants-usa-simi-valley', 88),
    ('Simi Childrens Dental Group', 'Simi Valley', 'Pediatric Dentistry / Orthodontics', '805-522-2164', 'https://www.simichildrensdentalgroup.com/', 'https://www.simichildrensdentalgroup.com/contact-dentist/', 91),
    ('ALFA Construction USA, Inc.', 'Simi Valley', 'Construction', '805-261-3700', 'https://www.alfaconstructionusa.com/', 'https://www.alfaconstructionusa.com/', 89),
    ('RE/MAX One - Simi Valley', 'Simi Valley', 'Real Estate Brokerage', '805-206-3776', 'https://www.maxonenews.com/simi-valley', 'https://www.maxonenews.com/simi-valley', 92),
    ('Keller Williams Exclusive Properties - Simi Valley', 'Simi Valley', 'Real Estate Brokerage', '805-777-7117', '', 'https://www.smart-sites.org/Office/KellerWilliamsRealty-107050', 92),
    ('Pinnacle Estate Properties - Simi Valley', 'Simi Valley', 'Real Estate Brokerage', '805-222-7000', 'https://pinnacleestate.com/', 'https://pinnacleestate.com/realestate/agents/12035/', 92),
]
