import sched, time, subprocess

s = sched.scheduler(time.time, time.sleep)
def cache_clear(sc):
    print('clearing cache...')
    rc = subprocess.call('/home/sema/gistapi/clear_db.sh')
    sc.enter(60, 1, cache_clear, (sc,))

s.enter(60, 1, cache_clear, (s,))
s.run()