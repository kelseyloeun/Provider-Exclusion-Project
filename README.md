# Provider Exclusion Database & Search Application

## Project Overview

The Provider Exclusion Database is a Python, PostgreSQL, and Django-based application designed to consolidate healthcare provider exclusion records from federal and state databases into a centralized, searchable system.

The project simplifies the process of looking up excluded healthcare providers by organizing information from multiple government sources into a relational database and providing a web interface for searching records.

## Technologies Used

- **Python** – Data extraction, cleaning, transformation, and database imports
- **PostgreSQL** – Relational database management
- **Django** – Backend web development and database integration
- **HTML/CSS** – Frontend website design
- **SQL** – Data queries, joins, constraints, and validation
- **Git/GitHub** – Version control and project documentation

## Data Sources

The database integrates publicly available exclusion records from four sources:

1. **HHS-OIG LEIE** – U.S. Department of Health and Human Services, Office of Inspector General, List of Excluded Individuals/Entities
2. **North Carolina Medicaid** – Excluded Providers List
3. **South Carolina Medicaid** – Sanctioned Individuals and Entities
4. **California Medi-Cal** – Suspended and Ineligible Provider List

Each imported record is associated with its original data source to maintain traceability.

## Database Structure

The PostgreSQL database uses five primary tables:

| Table | Description |
|---|---|
| `data_source` | Stores information about each federal or state exclusion data source |
| `import_log` | Tracks data imports, timestamps, status, and record counts |
| `excluded_party` | Stores individual and organizational provider information |
| `exclusion_record` | Stores exclusion records and links them to providers and sources |
| `identifier` | Stores provider identifiers, including NPIs and license numbers |

### Database Design

The database was designed using relational database principles, including:

- Primary and foreign keys to establish relationships
- `NOT NULL` constraints to maintain consistent data formatting
- Unique identifiers for individual database records
- Standardized placeholder values for missing information
- Separate
