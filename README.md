# NP-MAT — Network Port-Matrix Automation Tool

## Overview

**NP-MAT (Network Port-Matrix Automation Tool)** is a Python-based network engineering automation project designed to automate the creation of wireless access point (WAP) port assignments across network switch stacks.

The project was developed to replace a repetitive manual workflow with a structured and repeatable process. NP-MAT accepts site and switch-stack information, distributes wireless access points across available switches, generates device names, assigns switch ports, and exports the resulting port matrix to a CSV file.

The goal of the project is to improve consistency, reduce manual configuration effort, and demonstrate how Python can be applied to practical network engineering workflows.

---

## Key Features

- Automatically generates WAP names based on site and stack information
- Distributes WAPs as evenly as possible across switches within a stack
- Supports switch stacks containing different numbers of switches
- Automatically assigns reserved ports from the highest available switch ports
- Continues WAP numbering across related switch stacks within the same network closet
- Organizes stack information using structured Python dictionaries
- Produces formatted console output for review
- Exports the completed port matrix to CSV
- Automatically incorporates the site identifier into the generated CSV filename

---

## Technologies Used

- Python
- Python dictionaries
- Python lists
- Functions and modular programming
- CSV file handling
- Input validation
- Network engineering concepts
- Cisco-style switch interface naming

---

## Project Structure

NP-MAT separates major operations into individual Python functions and modules to improve readability, maintainability, and scalability.

Core functionality includes:

### `get_siteData`

Collects site-level information used throughout the program.

### `get_stackData`

Collects information about the switch stacks included in the network design.

### `get_WAPcount`

Determines the number of wireless access points associated with each switch stack.

### `distribute_waps`

Calculates how WAPs should be distributed across the switches within a stack.

For example, 10 WAPs across a four-switch stack may be distributed as:

```text
[3, 3, 2, 2]
```

This keeps the number of WAP connections per switch as balanced as possible.

### `get_WAPnames`

Automatically generates WAP names and maintains sequential numbering across related switch stacks.

### `reserve_ports`

Determines which switch interfaces should be assigned to WAPs using reserved ports near the highest-numbered interfaces on each switch.

---

## Example Workflow

NP-MAT follows a workflow similar to:

```text
Site Information
        ↓
Switch Stack Information
        ↓
WAP Counts
        ↓
WAP Distribution
        ↓
WAP Name Generation
        ↓
Switch-Port Assignment
        ↓
Formatted Output
        ↓
CSV Export
```

Each switch stack is represented using structured data similar to:

```python
stack_data = {
    "stkDC105a01a01": {
        "switch_count": 4,
        "wap_count": 10,
        "wap_distribution": [3, 3, 2, 2],
        "wap_names": [...],
        "reserved_ports": [...]
    }
}
```

This structure keeps the network information organized while allowing the program to process multiple switch stacks dynamically.

---

## Port Assignment Logic

NP-MAT reserves higher-numbered switch interfaces for wireless access points.

For a four-switch stack, assigned interfaces may include ports such as:

```text
Gi1/0/46
Gi2/0/46
Gi3/0/47
Gi4/0/47
Gi1/0/48
Gi2/0/48
Gi3/0/48
Gi4/0/48
```

The allocation logic distributes connections across stack members while maintaining predictable port assignments.

---

## WAP Naming Logic

NP-MAT also generates WAP names automatically.

For example:

```text
Switch Stack:
stkDC105a01a01

Generated WAPs:
wapDC105a01a01
wapDC105a01a02
wapDC105a01a03
...
```

When multiple stacks belong to the same logical closet or location, NP-MAT can continue the numbering sequence rather than restarting at the first WAP.

This provides consistent naming across related network infrastructure.

---

## CSV Export

After processing the network data, NP-MAT generates a CSV-based port matrix that can be used for engineering documentation and deployment planning.

The site identifier is automatically incorporated into the filename.

Example:

```text
DC105_WAP_Port_Matrix.csv
```

This allows generated files to be easily associated with their corresponding network design.

---

## Engineering Value

NP-MAT demonstrates how software automation can improve traditional network engineering workflows.

The project applies programming concepts including:

- Data structures
- Modular program design
- Algorithmic distribution
- Automated naming
- File generation
- Input processing
- Network interface mapping

By automating repetitive design tasks, the tool reduces the amount of manual work required to create network port matrices while improving consistency and repeatability.

NP-MAT was also my first completed programming project after earning my Computer Engineering degree and represents an important step in combining my network engineering experience with software development.

---

## Project Status

**Completed**

Core functionality includes:

- WAP distribution
- Automated WAP naming
- Switch-port assignment
- Closet-based numbering continuation
- Structured console output
- CSV export
- Site-based output filenames

---

## Disclaimer

All site identifiers, device names, network naming conventions, and example data shown in this project are **fictional and provided solely for demonstration purposes**.

The project does not contain production network information, proprietary company naming conventions, confidential infrastructure data, or customer information.
