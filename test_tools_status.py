#!/usr/bin/env python3
"""
Test current tools status
"""

print("=== CrewAI Tools Status ===")

# Test 1: Check crewai-tools import
try:
    import crewai_tools
    print(f"✅ crewai_tools imported: {crewai_tools.__version__ if hasattr(crewai_tools, '__version__') else 'unknown version'}")
    
    # Test specific tools
    try:
        from crewai_tools import SerperDevTool
        print("✅ SerperDevTool available")
    except ImportError as e:
        print(f"❌ SerperDevTool not available: {e}")
    
    try:
        from crewai_tools import ScrapeWebsiteTool
        print("✅ ScrapeWebsiteTool available")
    except ImportError as e:
        print(f"❌ ScrapeWebsiteTool not available: {e}")
        
except ImportError as e:
    print(f"❌ crewai_tools not available: {e}")

# Test 2: Check what's actually in crewai_tools
try:
    import crewai_tools
    print(f"\n📦 Available in crewai_tools: {dir(crewai_tools)}")
except:
    pass

print("\n=== Recommendation ===")
print("🎯 Current system works with 0 tools")
print("🔑 Add Serper API key for web search capabilities")
print("📊 System will use intelligent fallbacks otherwise")