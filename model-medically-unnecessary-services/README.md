# Medically Unnecessary Services

## Description
Identifies procedures that have not been performed but have been charged for by analyzing the patient's procedure, claim and diagnosis history.

## Product Overview
Identify procedures that have not been performed but have been charged for by analyzing a patient's procedure and diagnosis history, as well as physician details (including coding errors). This model, in basic terms, reverse engineers the main use case behind RevCaptureAi. It tries to identify medically unnecessary services in a healthcare claim. Using the input data of medical claims from an insurance company (i.e. common medical codes HCPCS, CPT, IDC10, REV, LOC), the model outputs a score of service necessity.

