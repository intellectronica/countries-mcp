import json
from typing import Any, Dict, List, Optional
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("countries")

# Load country data
try:
    with open("countries.json", "r", encoding="utf-8") as f:
        countries_data = json.load(f)
except FileNotFoundError:
    countries_data = []
    print("Warning: countries.json not found. Please ensure it is present in the working directory.")

def _get_country_by_name(name: str) -> List[Dict[str, Any]]:
    """Helper function to search countries by name."""
    results = []
    name_lower = name.lower()
    for country in countries_data:
        common = country.get("name", {}).get("common", "").lower()
        official = country.get("name", {}).get("official", "").lower()
        
        # Check for exact match first, or partial match
        if name_lower == common or name_lower == official or name_lower in common or name_lower in official:
            results.append(country)
    return results

@mcp.tool()
def list_countries() -> List[str]:
    """List all available country names (common names)."""
    return sorted([c.get("name", {}).get("common", "Unknown") for c in countries_data])

@mcp.tool()
def get_country_by_name(name: str) -> List[Dict[str, Any]]:
    """
    Search for countries by name. 
    Matches against common and official names.
    Returns a list of matching country objects.
    """
    return _get_country_by_name(name)

@mcp.tool()
def get_country_by_code(code: str) -> Optional[Dict[str, Any]]:
    """
    Get country information by ISO code.
    Supports CCA2 (2-letter), CCA3 (3-letter), or CCN3 (numeric) codes.
    """
    code_upper = code.upper()
    for country in countries_data:
        if (country.get("cca2") == code_upper or 
            country.get("cca3") == code_upper or 
            country.get("ccn3") == code):
            return country
    return None

@mcp.tool()
def get_country_currency(country_name: str) -> Optional[Dict[str, Any]]:
    """Get currency information for a specific country."""
    countries = _get_country_by_name(country_name)
    if countries:
        # Return the first match's currencies
        return countries[0].get("currencies")
    return None

@mcp.tool()
def get_country_capital(country_name: str) -> Optional[List[str]]:
    """Get the capital city(ies) of a country."""
    countries = _get_country_by_name(country_name)
    if countries:
        return countries[0].get("capital")
    return None

@mcp.tool()
def get_country_languages(country_name: str) -> Optional[Dict[str, str]]:
    """Get the languages spoken in a country."""
    countries = _get_country_by_name(country_name)
    if countries:
        return countries[0].get("languages")
    return None

@mcp.tool()
def filter_countries_by_region(region: str) -> List[str]:
    """
    Get a list of countries in a specific region.
    Common regions: Africa, Americas, Asia, Europe, Oceania, Antarctic.
    """
    results = []
    region_lower = region.lower()
    for country in countries_data:
        if country.get("region", "").lower() == region_lower:
            results.append(country.get("name", {}).get("common", "Unknown"))
    return sorted(results)

if __name__ == "__main__":
    mcp.run()
