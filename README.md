# ravenstack-saas-dashboard
# SaaS Metrics Dashboard (Streamlit)

## Overview

This project is an end-to-end **SaaS metrics dashboard** built with **Python and Streamlit**. 

Instead of visualizing every possible intermediate step, I deliberately focused on **executive-level KPIs** that answer one question:

> *“How is the business performing right now, and where should attention go?”*

The live dashboard is deployed publicly and accessible here:
[https://ravenstack-saas-dashboard.streamlit.app/](https://ravenstack-saas-dashboard.streamlit.app/)

---

## Problem Framing

Early in the project, I stepped back and reframed the problem:

* This is a **dashboard**, not an analysis notebook
* The end user is a **founder / product / operations lead**
* They care about **outcomes**, not raw transformations

That led me to design around **final KPIs**.

---

## Metrics Chosen (and Why)

I selected metrics that are:

* Actionable
* Common in SaaS reporting
* Interpretable at a glance

**Core KPIs displayed:**

* **Active Users** – product engagement
* **New Accounts** – growth signal
* **Churn Rate** – retention health

Notably, I deprioritized deeper breakdowns unless they directly supported a decision. This reflects how dashboards are actually used in practice.

---

## Design Decisions

### 1. KPI-First Layout

* Metrics are presented as **top-level cards**
* This avoids vertical scrolling and cognitive overload
* The layout mirrors real executive dashboards

### 2. Minimal but Clear Visuals

* Time-series charts are used only where trend matters
* No unnecessary filters or interactions at this stage

### 3. Streamlit as a Product Tool

* Streamlit was chosen to prioritize **speed, clarity, and deployment**
* The dashboard is meant to be *shared*, not just run locally

---

## Technical Stack

* **Python**
* **Streamlit**
* **Pandas**
* **Altair / Vega-Lite (for charts)**

The project uses a virtual environment (`.venv`) for dependency isolation.

---

## Deployment

The app is deployed using **Streamlit Community Cloud**

