# Literacy rate vs. average years of schooling - Data package

This data package contains the data that powers the chart ["Literacy rate vs. average years of schooling"](https://ourworldindata.org/grapher/literacy-rates-vs-average-years-of-schooling?v=1&csvType=full&useColumnShortNames=false) on the Our World in Data website.

### Active Filters

A filtered subset of the full data was downloaded. The following filters were applied:

## CSV structure

Each row is an observation for an entity (usually a country or region) at a timepoint.

- "Entity" — the name of the entity, e.g. "United States".
- "Code" — our internal entity code. For most countries this is the [ISO alpha-3](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-3) code, e.g. "USA"; historical and other non-standard entities get a custom code.
- "Year" or "Day" — the timepoint. Annual data has a "Year" column holding an integer year; otherwise a "Day" column holds a date string in the form "YYYY-MM-DD".
- Every remaining column is a data column, each one a time series. Downloaded with the "full data" option each corresponds to one time series below; with "only selected data visible in the chart" they are transformed depending on the chart type, so the correspondence may be less direct.


## Metadata.json structure

The .metadata.json file contains metadata about the data package. The "charts" key contains information to recreate the chart, like the title, subtitle etc. The "columns" key contains information about each of the columns in the csv, like the unit, timespan covered, citation for the data etc.

## How we process data at Our World in Data

Our World in Data is almost never the original producer of the data - almost all of the data we use has been compiled by others. If you want to re-use data, it is your responsibility to ensure that you adhere to the sources' license and to credit them correctly. Please note that a single time series may have more than one source - e.g. when we stitch together data from different time periods by different producers or when we calculate per capita metrics using population data from a second source.

Preparing this data involves several processing steps. Depending on the data, this can include standardizing country names and world region definitions, converting units, calculating derived indicators such as per capita measures, as well as adding or adapting metadata such as the name or the description given to an indicator.
[Read about our data pipeline](https://docs.owid.io/projects/etl/).

## Detailed information about each time series


### Literacy rate
Share of adults who can read and write a simple statement about their everyday life.
Last updated: May 12, 2026  
Next expected update: May 2027  
Date range: 1475–2024  
Unit: %  
Source: UNESCO (1957); UNESCO (1953); Buringh and van Zanden (2009); van Zanden, J. et al.; UNESCO Institute for Statistics (2026) – with major processing by Our World in Data  

#### How to cite this data

UNESCO (1957) and other sources – with major processing by Our World in Data

#### What you should know about this data
- Literacy is a foundational skill. Children need to learn to read so that they can read to learn. When we fail to teach this foundational skill, people have fewer opportunities to lead the rich and interesting lives that a good education offers. This indicator measures the percentage of people aged 15 and older who can read and write a simple sentence about their daily life.
- Historical data shows that only a very small share of the population, a tiny elite, was able to read and write. Although literacy has increased over the last few generations, it remains an important challenge for our time to [provide this foundational skill to all](https://ourworldindata.org/better-learning).
- However, measuring literacy over time is difficult, as definitions of what it means to be “literate” have varied widely across countries and historical periods. As a result, comparisons should be made with caution.
- Our team investigated the strengths and shortcomings of the available data on literacy. Based on this work, we've combined historical and contemporary literacy rates from various sources to provide a long-term view of global literacy trends from 1451 to the present. For detailed information on where each data point comes from, you can view and download this [Google Sheet](https://docs.google.com/spreadsheets/d/1FZTCa7pk7euLteLcaIWgmUzGUuNVLM-myXFkqQcv93A/edit).
- Many developed countries have discontinued literacy tracking as rates approached universal levels by the late 20th century, making measurement less relevant for policy purposes.
- All of this data measures basic literacy — can you read simple text and write your name? It doesn't capture *functional* literacy — can you understand a job application or follow written instructions? That requires years more education and is much harder to measure historically.

#### How this data is described by its producers
The current UNESCO standard for defining literacy is the percentage of the population aged 15 and above who can read, understand, and write a short, simple statement on their everyday life. Generally, “literacy” also encompasses “numeracy”, the ability to make simple arithmetic calculations.

#### Notes on our processing step for this indicator
- This dataset combines historical and contemporary literacy rates from various sources to provide a long-term view of global literacy trends from 1451 to the present.
- 1451–1800: Direct literacy surveys did not exist during this period. Data for Great Britain, Ireland, France, Belgium, the Netherlands, Germany, Italy, Spain, Sweden, and Poland comes from the "[Charting the Rise of the West](https://www.researchgate.net/publication/46544350_Charting_the_Rise_of_the_West_Manuscripts_and_Printed_Books_in_Europe_A_Long-Term_Perspective_from_the_Sixth_through_Eighteenth_Centuries)" study. The authors estimated literacy rates using manuscript and book production as indirect indicators. While more books likely indicated more readers, this approach has clear limitations.
- 1820–1970 (Global estimates): Estimates for worldwide literacy are drawn from the OECD's “[How Was Life? Global Wellbeing Since 1820](https://www.oecd.org/en/publications/how-was-life_9789264214262-en.html)” report, which compiled a global long-run estimate of literacy using available historical records. A key limitation is that early literacy measures often accepted minimal skills — such as the ability to sign marriage documents — which fall short of contemporary literacy standards involving actual reading and writing proficiency.
- 1900–1950: UNESCO's “[Progress of literacy in various countries](https://unesdoc.unesco.org/ark:/48223/pf0000002898)” gathered data from 26 countries, revealing substantial variation in definitions. Some countries required only reading or writing skills, others demanded both, and some accepted signature ability as sufficient proof. Age thresholds also varied widely, ranging from 5 to 15 years.
- 1950: UNESCO's “[World Illiteracy at Mid-Century](https://unesdoc.unesco.org/ark:/48223/pf0000002930)” marked a significant milestone as the first comprehensive global literacy assessment. Data primarily came from censuses conducted between 1945 and 1954 for populations aged 15 and older. Where census data was unavailable, researchers generated estimates using historical trends and country-specific factors. Given the uncertainty, literacy rates were reported in 5% intervals. This data is reported as a range (e.g., 10–20%). These ranges were converted into single-point estimates by taking their midpoint to allow for consistent analysis. For example, 10–20% was recoded as 15%.
- 1970–present: Contemporary data comes from the [UNESCO Institute for Statistics](https://databrowser.uis.unesco.org/resources/bulk), based on population censuses or household surveys, and is often self-reported. A person is considered literate if they can read and write a short, simple sentence about everyday life. Many countries also include basic numeracy in this definition. Rates are shown as the percentage of the population aged 15 and above who meet this threshold.
- When only the illiteracy rate was reported, the literacy rate was calculated by subtracting it from 100%.


### Average years of education for 15-64 years olds
Average years of formal education for individuals aged 15-64.
Last updated: July 17, 2023  
Date range: 1870–2040  
Unit: years  
Source: Barro and Lee (2015); Lee and Lee (2016) – with major processing by Our World in Data  

#### How to cite this data

Barro and Lee (2015); Lee and Lee (2016) – with major processing by Our World in Data

#### What you should know about this data
- For the years leading up to 2015, the data are derived from historical estimates, providing a retrospective view of education levels. For the years 2015 and beyond, the projections are grounded in the historical data of 2010, which serve as the foundational benchmark. These forward-looking projections are then crafted by analyzing trends in school enrollment and changes in population structures. These trends are informed by forecasts from the United Nations, ensuring a global perspective and understanding of future educational developments.
- The method to estimate average years of schooling takes into account the age distribution in the population. This is important because access to education can vary significantly across generations. Older generations may have had fewer educational opportunities than younger ones, which affects the overall average education level.
- It also considers the typical duration required to complete each education level. For instance, primary education usually takes about 6 years, secondary education 4-6 years, and higher education may take even longer. Understanding the time investment required for different education levels is essential for accurate assessment.
- At its core, the method calculates the average years of schooling. This is achieved by determining the percentage of the population that has completed each education level and multiplying it by the duration of that level. The sum of these results gives a comprehensive view of both the extent of educational attainment and the time spent in education by the population.
- The method is dynamic, adapting to changes over time and across regions. For example, if a country increases the length of primary education, this change is included in subsequent calculations. This adaptability ensures that the average years of education remain relevant and accurate over time and across different educational systems.
- Note that the method does not take into account the quality of education. It only considers the number of years spent in education. This means that the average years of schooling may not reflect the actual skills and knowledge of the population.

#### Notes on our processing step for this indicator
Historical data up to the year 2010 has been sourced from 'Human Capital in the Long Run' by Lee and Lee (2016). This historical data was then combined with recent projections provided by Barro ane Lee (2015).

Regional aggregates were computed by Our World in Data through yearly population-weighted averages, where annual values are proportionally adjusted to emphasize the influence of larger populations.



### Population
Population by country, available from 10,000 BCE to 2023, based on data and estimates from different sources.
Last updated: July 15, 2024  
Next expected update: December 2026  
Date range: 10000 BCE – 2023 CE  
Unit: people  
Source: HYDE (2023); Gapminder (2022); UN WPP (2024) – with major processing by Our World in Data  

#### How to cite this data

HYDE (2023); Gapminder (2022); UN WPP (2024) – with major processing by Our World in Data

#### What you should know about this data
- Population is the most commonly used metric throughout Our World in Data. It is used directly to understand population growth over time, and indirectly to calculate per-capita indicators, making it easier to compare countries of different sizes.
- We construct this indicator by combining multiple sources covering different periods.
  - HYDE v3.3 (2023): historical estimates from 10,000 BCE to 1799.
  - Gapminder v7 (2022): for 1800-1949.
  - UN World Population Prospects (2024): for 1950 onwards, including 2100 projections.
  - Gapminder Systema Globalis (2023): additional source for former countries (Yugoslavia, USSR, etc.)
- Breaks in the data may occur at the boundaries between sources due to their methodological differences.
- You can read more about the sources and methodology in our [dedicated article](https://ourworldindata.org/population-sources). We also provide a table of sources showing the source we use for each country-year.
- We calculate geographical aggregates (continents, income groups, etc.) by summing individual country populations. For years before 1800, we rely directly on HYDE's values for continents to ensure historical consistency.

#### Notes on our processing step for this indicator
### Combination of different sources
We construct our long-run population data by combining multiple sources:

- 10,000 BCE–1799: historical estimates by HYDE (v3.3).

- 1800–1949: historical estimates by Gapminder (v7).

- 1950–2023: population records from the United Nations World Population Prospects (2024 revision).

**Geographical aggregates**

- For most years, we calculate aggregates by summing the population of member countries.
- We do this based on [our definition of continents](https://ourworldindata.org/world-region-map-definitions#our-world-in-data) and the [World Bank’s income groups](https://ourworldindata.org/grapher/world-bank-income-groups).
- The only exception is before 1800, where we use HYDE's estimates for continents (but not income groups).

For most of the years, we've estimated regional aggregates by summing the population of countries in each region. We've relied on [our continents](https://ourworldindata.org/world-region-map-definitions#our-world-in-data) and [World Bank income group definitions](https://ourworldindata.org/grapher/world-bank-income-groups). The only exception is before 1800, where we've used HYDE's estimates on continents (but not income groups).

**World**
- Before 1800: we use data from HYDE.
- 1800-1950: we estimate the global population by summing all available countries in the dataset.
- After 1950, we rely on estimates from the United Nations World Population Prospects.


### World region according to OWID
Regions defined by Our World in Data, which are used in OWID charts and maps.
Last updated: January 1, 2023  
Date range: 2023–2023  
Source: Our World in Data  

#### How to cite this data

Our World in Data


## Sources

These are the sources behind the data in this package. Each time series above names the ones it draws on in its citation.

### UNESCO – World illiteracy at mid-century

This dataset gives an early global picture of adult literacy, using data mostly collected between 1945 and 1954. UNESCO estimated illiteracy rates for people aged 15 and over. In many cases, the numbers came from recent censuses. Where data were missing or outdated, estimates were made using past trends, school or military records, or general information about each country.

Because the data was not always complete, most illiteracy rates are shown in 5% steps. Even in countries with high literacy, a small number of people—about 1–2%—were assumed to be unable to learn to read or write due to disabilities. The estimates use a simple definition of literacy: being able to read or to read and write.

Producer: UNESCO  
Published: 1957  
Retrieved on: 2025-06-10  
Retrieved from: https://unesdoc.unesco.org/ark:/48223/pf0000002930  
License: CC BY 3.0 IGO (https://databrowser.uis.unesco.org/terms-and-conditions)  

Citation: UNESCO. (1957). World illiteracy at mid-century: A statistical study. United Nations Educational, Scientific and Cultural Organization.

### UNESCO – Progress of literacy in various countries

This dataset presents UNESCO’s first global survey of adult illiteracy, based on census and official government data from 26 countries. Countries were included if they had illiteracy data for at least three census years since around 1900. The dataset uses the most recent available figures and shows how literacy levels changed over time in the first half of the 20th century.

The study notes that countries defined and measured literacy in different ways. Some counted people as literate if they could read or write; others required more, like writing a letter or reading a passage. In some places, being able to sign one’s name was enough; in others, it was not. The age at which people were counted also varied—from as young as 5 to as old as 15.

These differences make it hard to compare literacy rates across countries or even across time within a country. People who could only read or only write were classified differently depending on local rules. Other issues, like missing data and unclear definitions, add to the difficulty. Despite these limits, the dataset offers important insights into global literacy patterns during this period.

Producer: UNESCO  
Published: 1953  
Retrieved on: 2025-06-10  
Retrieved from: https://unesdoc.unesco.org/ark:/48223/pf0000002898  
License: CC BY 3.0 IGO (https://databrowser.uis.unesco.org/terms-and-conditions)  

Citation: UNESCO. (1953). Progress of literacy in various countries: a preliminary statistical study of available census data since 1900. United Nations Educational, Scientific and Cultural Organization.

### Buringh and van Zanden – Charting the “Rise of the West”: Manuscripts and Printed Books in Europe, A Long-Term Perspective from the Sixth through Eighteenth Centuries

This paper presents estimates of the production of manuscripts and printed books in Western Europe over a span of thirteen centuries. To estimate literacy levels, the authors first calculate book consumption per capita, then convert these figures into literacy rates using two key inputs: historical trends in book prices and an assumed elasticity of demand for books. The book price data are sourced from the work of Jan Luiten van Zanden and Gregory Clark, while the elasticity of demand—reflecting how book consumption responds to price changes—is set at 1.4, based on contemporary economic literature. This method assumes that lower book prices made books more accessible, which in turn helped to increase literacy rates.

Producer: Buringh and van Zanden  
Published: 2009  
Retrieved on: 2025-06-09  
Retrieved from: https://www.researchgate.net/publication/46544350_Charting_the_Rise_of_the_West_Manuscripts_and_Printed_Books_in_Europe_A_Long-Term_Perspective_from_the_Sixth_through_Eighteenth_Centuries  
Direct download: https://www.researchgate.net/profile/Jan-Zanden/publication/46544350_Charting_the_Rise_of_the_West_Manuscripts_and_Printed_Books_in_Europe_A_Long-Term_Perspective_from_the_Sixth_through_Eighteenth_Centuries/links/00b49528a18ffc6638000000/Charting-the-Rise-of-the-West-Manuscripts-and-Printed-Books-in-Europe-A-Long-Term-Perspective-from-the-Sixth-through-Eighteenth-Centuries.pdf?_tp=eyJjb250ZXh0Ijp7ImZpcnN0UGFnZSI6InB1YmxpY2F0aW9uIiwicGFnZSI6InB1YmxpY2F0aW9uIn19  
License: CC BY 4.0  

Citation: Buringh, E., & van Zanden, J. L. (2009). Charting the “Rise of the West”: Manuscripts and printed books in Europe, a long‐term perspective from the sixth through the eighteenth centuries. The Journal of Economic History, 69(2), 409–445. https://doi.org/10.1017/S0022050709000837

### van Zanden, J. et al. – How Was Life? Global Well-being since 1820 – Education

The data comes from the How Was Life? Global Well-being Since 1820 report by the OECD. It notes that the concept of literacy has changed over time, which affects how it is measured. In earlier periods, literacy was broadly understood as being “educated” or “learned.” However, by the late 19th century, the definition narrowed to mean the ability to read and write simple texts. This shift in meaning was driven by the spread of mass education, which emphasized basic reading and writing skills for large populations. As a result, historical estimates of literacy are based on differing definitions over time, making it important to interpret the data within its historical context.

Producer: van Zanden, J. et al.  
Retrieved on: 2023-08-14  
Retrieved from: https://www.oecd-ilibrary.org/economics/how-was-life/education-since-1820_9789264214262-9-en  
License: Creative Commons BY 4.0 (https://www.oecd.org/termsandconditions/)  

Citation: van Zanden, J., et al. (eds.) (2014), How Was Life?: Global Well-being since 1820, Education, OECD Publishing, Paris. Available at https://www.oecd-ilibrary.org/economics/how-was-life/education-since-1820_9789264214262-9-en. Accessed on 14th August 2023.

### UNESCO Institute for Statistics – UNESCO Institute for Statistics (UIS) – Education

The UNESCO Institute for Statistics (UIS) is the official and trusted source of internationally-comparable data on education, science, culture and communication. As the official statistical agency of UNESCO, the UIS produces a wide range of state-of-the-art databases to fuel the policies and investments needed to transform lives and propel the world towards its development goals. The UIS provides free access to data for all UNESCO countries and regional groupings from 1970 to the most recent year available.

Producer: UNESCO Institute for Statistics  
Published: 2026-02-01  
Retrieved on: 2026-05-12  
Retrieved from: https://databrowser.uis.unesco.org/resources/bulk  
Direct download: https://download.uis.unesco.org/bdds/202602/SDG.zip  
License: CC BY 3.0 IGO (https://databrowser.uis.unesco.org/terms-and-conditions)  

Citation: UNESCO Institute for Statistics (UIS), Education, https://uis.unesco.org/bdds, 2026.

### Barro and Lee – Projections of Educational Attainment

Using the estimates on school enrollment and population structure, Barro and Lee have constructed projections of educational attainment for the population, disaggregated by gender and age group (15–24, 25–64, and 15–64) for 146 countries from 2015 to 2040 at five-year intervals.

They first use the 2010 data on educational attainment by age group as benchmark figures to project the educational attainment of the population by age group for the next three decades. They then estimate the distribution of educational attainment for the younger population, aged 15-24, at the five-year intervals from 2015 to 2040 and then forward-extrapolate the estimates to construct the distribution of educational attainment for the older population groups. For the population structure, they use existing U.N. projections. For the detailed explanation of the estimation method, see Barro and Lee (2015, chapter 3).

Producer: Barro and Lee  
Published: 2015  
Retrieved on: 2023-11-20  
Retrieved from: http://www.barrolee.com/  
License: 2021 by Robert J. Barro and Jong-Wha Lee. (https://barrolee.github.io/BarroLeeDataSet/OUPProj.html)  

Citation: Barro, Robert J. and Jong-Wha Lee, Education Matters: Global Schooling Gains from the 19th to the 21st Century (Oxford University Press, 2015)

### Lee and Lee – Human Capital in the Long Run

Datasets on estimated school enrollment ratios from 1820 to 2010 and estimated educational attainment for the total, female, and male populations from 1870 to 2010. The estimates are available in five-year intervals for 111 countries.

Datasets were last updated in 2021 September. The research provides insightful analysis on the progression and trends of educational attainment over a long historical period, offering a comprehensive understanding of educational developments globally.

Producer: Lee and Lee  
Published: 2016  
Retrieved on: 2023-11-20  
Retrieved from: https://barrolee.github.io/BarroLeeDataSet/DataLeeLee.html  
License: 2021 by Robert J. Barro and Jong-Wha Lee. (https://barrolee.github.io/BarroLeeDataSet/OUPProj.html)  

Citation: Lee, Jong-Wha and Hanol Lee, 2016, “Human Capital in the Long Run,” Journal of Development Economics, vol. 122, pp. 147-169.

### PBL Netherlands Environmental Assessment Agency – History Database of the Global Environment

This database presents an update and expansion of the History Database of the Global Environment (HYDE, v 3.3) and replaces former HYDE 3.2 version from 2017. HYDE is and internally consistent combination of updated historical population estimates and land use. Categories include cropland, with a new distinction into irrigated and rain fed crops (other than rice) and irrigated and rain fed rice. Also grazing lands are provided, divided into more intensively used pasture, converted rangeland and non-converted natural (less intensively used) rangeland. Population is represented by maps of total, urban, rural population and population density as well as built-up area. The period covered is 10 000 BCE to 2023 CE. Spatial resolution is 5 arc minutes (approx. 85 km2 at the equator), the files are in ESRI ASCII grid format.

Producer: PBL Netherlands Environmental Assessment Agency  
Published: 2023-11-30  
Retrieved on: 2024-01-02  
Retrieved from: https://doi.org/10.24416/UU01-AEZZIT  
Direct download: https://geo.public.data.uu.nl/vault-hyde/HYDE%203.3%5B1701183392%5D/original/hyde33_c7_base_mrt2023/txt/all_indicators.zip  
License: CC BY 4.0 (https://doi.org/10.24416/UU01-AEZZIT)  

Citation: Utrecht University/PBL Netherlands Environmental Assessment Agency – History Database of the Global Environment (HYDE v 3.3, 2023).
Klein Goldewijk, C.G.M., Beusen, A., Doelman, J., Stehfest, E., 2017, Anthropogenic land use estimates for the Holocene – HYDE 3.2, Earth Syst. Sci. Data, 9, 927–953

### Gapminder – Population

Gapminder's population data is divided into two chunks: One long historical trend for the global population that goes back to 10,000 BC. And the second chunk is country estimates that only reaches back to 1800.

For the first chunk, several sources were used. You can learn more at https://docs.google.com/spreadsheets/d/1hkLbEilJbl630IG68q-aQJlUjuTFm9b_12nQMVd1sZM/edit#gid=0. For the second chunk, Gapminder uses UN population data between 1950 to 2100 from the UN Population Division World Population Prospects 2019, and the forecast to the year 2100 uses their medium-fertility variant.

For years before 1950, this version uses the data documented in greater detail by Mattias Lindgren in version 3. The main source was Angus Maddison's data, which CLIO Infra Project maintained and improved. Note that when combining version 3 with the new UN data, the trends for a few countries didn't match up in the overlapping year 1950.

Minor adjustments were made to the years before and after to smooth out discrepancies between the two sources and avoid spurious jumps in Gapminder's visualizations.

Visit https://www.gapminder.org/data/documentation/gd003/ to learn more about the methodology used and the data from back to 10,000 BC.

Producer: Gapminder  
Published: 2022-10-19  
Retrieved on: 2023-03-31  
Retrieved from: http://gapm.io/dpop  
Direct download: https://gapm.io/dl_popv7  
License: CC BY 4.0 (https://docs.google.com/document/d/1-RmthhS2EPMK_HIpnPctcXpB0n7ADSWnXa5Hb3PxNq4/edit?usp=sharing)  

Citation: Gapminder Population v7 (2022)

### United Nations – World Population Prospects

World Population Prospects 2024 is the 28th edition of the official estimates and projections of the global population that have been published by the United Nations since 1951. The estimates are based on all available sources of data on population size and levels of fertility, mortality and international migration for 237 countries or areas. If you have questions about this dataset, please refer to [their FAQ](https://population.un.org/wpp/faqs). You can also explore [data sources](https://population.un.org/wpp/data-sources) for each country or visit [their main page](https://population.un.org/wpp/) for more details.

Producer: United Nations  
Published: 2024-07-11  
Retrieved on: 2024-07-11  
Retrieved from: https://population.un.org/wpp/downloads/  
Direct download: https://population.un.org/wpp/assets/Excel%20Files/1_Indicator%20(Standard)/CSV_FILES/WPP2024_PopulationBySingleAgeSex_Medium_1950-2023.csv.gz  
License: CC BY 3.0 IGO (https://population.un.org/wpp/downloads/)  

Citation: United Nations, Department of Economic and Social Affairs, Population Division (2024). World Population Prospects 2024, Online Edition.

### United Nations – World Population Prospects – Interim Update

World Population Prospects 2024 is the 28th edition of the official estimates and projections of the global population that have been published by the United Nations since 1951. The estimates are based on all available sources of data on population size and levels of fertility, mortality and international migration for 237 countries or areas. If you have questions about this dataset, please refer to [their FAQ](https://population.un.org/wpp/faqs). You can also explore [data sources](https://population.un.org/wpp/data-sources) for each country or visit [their main page](https://population.un.org/wpp/) for more details.

This is an interim update containing revised medium-variant estimates and projections for Togo.

Producer: United Nations  
Published: 2026-01-19  
Retrieved on: 2026-03-31  
Retrieved from: https://population.un.org/wpp/downloads/  
Direct download: https://population.un.org/wpp/assets/Excel%20Files/1_Indicator%20(Standard)/WPP2024_CSV_files_update.zip  
License: CC BY 3.0 IGO (https://population.un.org/wpp/downloads/)  

Citation: United Nations, Department of Economic and Social Affairs, Population Division (2024). World Population Prospects 2024, Online Edition.

### Gapminder – Systema Globalis

Data by Gapminder on population and other indicators. It provides data on former countries and regions.

Producer: Gapminder  
Published: 2023-02-21  
Retrieved on: 2023-03-31  
Retrieved from: https://github.com/open-numbers/ddf--gapminder--systema_globalis  
License: CC BY 4.0 (https://github.com/open-numbers/ddf--gapminder--systema_globalis)  

Citation: Gapminder – Systema Globalis (2023)

### Our World in Data – Regions

Producer: Our World in Data  

    