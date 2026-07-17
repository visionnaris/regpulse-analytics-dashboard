terraform {
  required_version = ">= 1.6.0"

  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "5.47"
    }
  }
}

provider "google" {
  skip_credentials_validation = true
  project = "tensile-oarlock-500904-d4"
  region  = "us-central1"
}

# Step 1: Create BigQuery dataset
resource "google_bigquery_dataset" "eu_regulations" {
  dataset_id = "eu_regulations_dev"
  location   = "US"
}

# Step 2: Create BigQuery table
resource "google_bigquery_table" "eu_regulations_table" {
  dataset_id = google_bigquery_dataset.eu_regulations.dataset_id
  table_id   = "EU_Regulations"

  schema = <<EOF
[
  {"name":"Framework","type":"STRING","mode":"REQUIRED"},
  {"name":"Regulations","type":"STRING","mode":"REQUIRED"},
  {"name":"EffectiveDate","type":"DATE","mode":"NULLABLE"},
  {"name":"DepartmentImpacted","type":"STRING","mode":"REQUIRED"},
  {"name":"KeyFocus","type":"STRING","mode":"REQUIRED"},
  {"name":"PenaltyRange","type":"STRING","mode":"REQUIRED"},
  {"name":"OperationalComplexity","type":"STRING","mode":"REQUIRED"},
  {"name":"RegulatorySeverity","type":"STRING","mode":"REQUIRED"},
  {"name":"BusinessImpact","type":"STRING","mode":"REQUIRED"},
  {"name":"FinancialPenaltyRisk","type":"STRING","mode":"REQUIRED"},
  {"name":"AIGovernanceScore","type":"INTEGER","mode":"REQUIRED"},
  {"name":"AIConfidenceScore","type":"STRING","mode":"REQUIRED"}
]
EOF
}

# Step 3: Insert all 10 rows
resource "google_bigquery_table_data" "eu_regulations_rows" {
  dataset_id = google_bigquery_dataset.eu_regulations.dataset_id
  table_id   = google_bigquery_table.eu_regulations_table.table_id

  rows = [
    {
      insert_id = "1"
      json = {
        Framework            = "EU AI Act"
        Regulations          = "Annex III (5)(b) Creditworthiness, Art. 27 FRIA, Art. 14 Human Oversight"
        EffectiveDate        = "2026-08-02"
        DepartmentImpacted   = "Loans"
        KeyFocus             = "High-risk AI credit scoring; human oversight required"
        PenaltyRange         = "€35M or 7% turnover"
        OperationalComplexity= "High"
        RegulatorySeverity   = "Very High"
        BusinessImpact       = "Direct impact on lending"
        FinancialPenaltyRisk = "Severe"
        AIGovernanceScore    = 97
        AIConfidenceScore    = "High"
      }
    },
    {
      insert_id = "2"
      json = {
        Framework            = "EU AI Act"
        Regulations          = "Art. 50 Transparency, Annex III Biometric ID"
        EffectiveDate        = "2026-12-02"
        DepartmentImpacted   = "KYC"
        KeyFocus             = "Automated decision disclosure; biometric restrictions"
        PenaltyRange         = "€10–35M"
        OperationalComplexity= "High"
        RegulatorySeverity   = "High"
        BusinessImpact       = "Customer onboarding risk"
        FinancialPenaltyRisk = "High"
        AIGovernanceScore    = 95
        AIConfidenceScore    = "High"
      }
    },
    {
      insert_id = "3"
      json = {
        Framework            = "EU AI Act"
        Regulations          = "Annex III Fraud Detection Models"
        EffectiveDate        = "2026-08-02"
        DepartmentImpacted   = "Payments"
        KeyFocus             = "AI fraud detection classified as high-risk"
        PenaltyRange         = "€20M or 4% turnover"
        OperationalComplexity= "Medium"
        RegulatorySeverity   = "High"
        BusinessImpact       = "Payment continuity"
        FinancialPenaltyRisk = "Moderate"
        AIGovernanceScore    = 92
        AIConfidenceScore    = "Medium-High"
      }
    },
    {
      insert_id = "4"
      json = {
        Framework            = "DORA"
        Regulations          = "Articles 5–14 ICT Risk Management"
        EffectiveDate        = "2025-01-17"
        DepartmentImpacted   = "Cyber Security"
        KeyFocus             = "ICT resilience, incident reporting, vendor oversight"
        PenaltyRange         = "2% turnover"
        OperationalComplexity= "High"
        RegulatorySeverity   = "High"
        BusinessImpact       = "Service continuity"
        FinancialPenaltyRisk = "Moderate"
        AIGovernanceScore    = 90
        AIConfidenceScore    = "Medium"
      }
    },
    {
      insert_id = "5"
      json = {
        Framework            = "DORA"
        Regulations          = "ICT Third-Party Oversight"
        EffectiveDate        = "2025-01-17"
        DepartmentImpacted   = "Deposits"
        KeyFocus             = "Cloud vendor resilience for deposit systems"
        PenaltyRange         = "2% turnover"
        OperationalComplexity= "Medium"
        RegulatorySeverity   = "Medium"
        BusinessImpact       = "Operational resilience"
        FinancialPenaltyRisk = "Moderate"
        AIGovernanceScore    = 88
        AIConfidenceScore    = "Medium"
      }
    },
    {
      insert_id = "6"
      json = {
        Framework            = "GDPR"
        Regulations          = "Art. 22 Automated Decisions, Art. 35 DPIA"
        EffectiveDate        = "2018-05-25"
        DepartmentImpacted   = "AML"
        KeyFocus             = "Human review for automated AML alerts; DPIA for transaction monitoring"
        PenaltyRange         = "€20M or 4% turnover"
        OperationalComplexity= "Medium"
        RegulatorySeverity   = "High"
        BusinessImpact       = "AML compliance risk"
        FinancialPenaltyRisk = "High"
        AIGovernanceScore    = 92
        AIConfidenceScore    = "High"
      }
    },
    {
      insert_id = "7"
      json = {
        Framework            = "GDPR"
        Regulations          = "Arts. 13–14 Transparency"
        EffectiveDate        = "2018-05-25"
        DepartmentImpacted   = "Wealth Management"
        KeyFocus             = "Transparency in profiling and robo-advisory"
        PenaltyRange         = "€20M or 4% turnover"
        OperationalComplexity= "Medium"
        RegulatorySeverity   = "Medium"
        BusinessImpact       = "Client trust"
        FinancialPenaltyRisk = "Moderate"
        AIGovernanceScore    = 90
        AIConfidenceScore    = "Medium-High"
      }
    },
    {
      insert_id = "8"
      json = {
        Framework            = "Basel III / CRR / CRD"
        Regulations          = "Capital Adequacy, Liquidity Coverage"
        EffectiveDate        = "2026-01-01"
        DepartmentImpacted   = "Treasury"
        KeyFocus             = "Risk-weighted capital buffers, liquidity stress testing"
        PenaltyRange         = "Supervisory fines + capital surcharges"
        OperationalComplexity= "High"
        RegulatorySeverity   = "Very High"
        BusinessImpact       = "Balance sheet resilience"
        FinancialPenaltyRisk = "Severe"
        AIGovernanceScore    = 88
        AIConfidenceScore    = "Medium"
      }
    },
    {
      insert_id = "9"
      json = {
        Framework            = "Basel III / CRR / CRD"
        Regulations          = "Leverage Ratios"
        EffectiveDate        = "2026-01-01"
        DepartmentImpacted   = "Deposits"
        KeyFocus             = "Stable funding requirements"
        PenaltyRange         = "Supervisory fines"
        OperationalComplexity= "Medium"
        RegulatorySeverity   = "High"
        BusinessImpact       = "Deposit stability"
        FinancialPenaltyRisk = "Moderate"
        AIGovernanceScore    = 87
        AIConfidenceScore    = "Medium"
      }
    },
    {
      insert_id = "10"
      json = {
        Framework            = "EBA Guidelines"
        Regulations          = "Internal Governance, Outsourcing, AML/KYC"
        EffectiveDate        = "2026-07-01"
        DepartmentImpacted   = "Loans, KYC, Payments"
        KeyFocus             = "Governance of AI models, AML transaction monitoring, outsourcing oversight"
        PenaltyRange         = "Supervisory sanctions"
        OperationalComplexity= "Medium-High"
        RegulatorySeverity   = "High"
        BusinessImpact       = "Compliance overhead"
        FinancialPenaltyRisk = "Moderate"
        AIGovernanceScore    = 90
        AIConfidenceScore    = "Medium-High"
      }
    }
  ]
}
