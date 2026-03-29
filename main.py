import sentinel_module

def run_sentinel():
    print("="*40)
    print(" INITIALIZING SENTINEL SYSTEM AUDIT ")
    print("="*40)
    
    # Running security log first 
    print(f"[SECURITY] {sentinel_module.log_event()}")
    
    # displaying hardware stats
    print(f"\n[CPU] Current Load: {sentinel_module.cpu_usage()}")
    print(f"[RAM] {sentinel_module.ram_info()}")
    print(f"[DISK] {sentinel_module.get_disk_space()}")
    
    print("\n" + "="*40)
    print(" AUDIT COMPLETE ")
    print("="*40)

if __name__ == "__main__":
    run_sentinel()