#!/usr/bin/env python3
"""
Test script to verify CrewAI integration fixes
"""

import asyncio
import logging
import sys
import os

# Add project root to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

async def test_crewai_integration():
    """Test CrewAI integration"""
    print("🧪 Testing CrewAI Integration...")
    
    try:
        from src.data.crewai_collector import get_crewai_collector, CREWAI_AVAILABLE
        
        print(f"✅ CrewAI Available: {CREWAI_AVAILABLE}")
        
        if CREWAI_AVAILABLE:
            # Test with dummy API key
            collector = get_crewai_collector("dummy_key")
            print(f"✅ Collector Enabled: {collector.enabled}")
            
            # Test fallback symbols
            symbols = await collector.get_available_symbols()
            print(f"✅ Got {len(symbols)} symbols")
            print(f"📊 First 5 symbols: {[s['symbol'] for s in symbols[:5]]}")
            
        else:
            print("⚠️ CrewAI not available, but system should still work with fallbacks")
            
    except Exception as e:
        print(f"❌ CrewAI test failed: {e}")
        import traceback
        traceback.print_exc()

async def test_vnstock_integration():
    """Test VNStock integration"""
    print("\n🧪 Testing VNStock Integration...")
    
    try:
        from src.data.vn_stock_api import VNStockAPI
        
        api = VNStockAPI()
        
        # Test with a valid VN stock
        test_symbol = "VCB"
        print(f"📈 Testing {test_symbol}...")
        
        data = await api.get_stock_data(test_symbol)
        if data:
            print(f"✅ Got data for {test_symbol}: {data.price:,.0f} VND")
        else:
            print(f"⚠️ No data for {test_symbol}, using fallback")
            
        # Test symbols list
        symbols = await api.get_available_symbols()
        print(f"✅ Got {len(symbols)} available symbols")
        
        # Check if using real data
        is_real = api.is_using_real_data()
        print(f"📊 Using real CrewAI data: {is_real}")
        
    except Exception as e:
        print(f"❌ VNStock test failed: {e}")
        import traceback
        traceback.print_exc()

async def main():
    """Main test function"""
    print("🚀 Starting Integration Tests...\n")
    
    await test_crewai_integration()
    await test_vnstock_integration()
    
    print("\n✅ Tests completed!")
    print("\n💡 Key Points:")
    print("- If CrewAI is not fully available, the system uses fallback data")
    print("- VNStock errors are now suppressed to reduce log spam")
    print("- The system should work even without all dependencies")

if __name__ == "__main__":
    asyncio.run(main())