##0x19. Postmortem

## Issue Summary

**Duration**: August 14, 2024, 2:00 AM to August 14, 2024, 4:30 AM (UTC)  
**Impact**: Approximately 60% of users were unable to access the main service, receiving "503 Service Unavailable" errors. This outage significantly affected business operations, particularly preventing transactions and access to the service during the affected time.  
**Root Cause**: The outage was caused by a bug in a recent deployment that led to improper handling of database connections, resulting in connection pool exhaustion.

## Timeline

- **2:00 AM**: Monitoring tools detected a spike in 503 errors and alerted the on-call engineer through PagerDuty.
- **2:05 AM**: On-call engineer acknowledged the alert and began investigating the issue.
- **2:15 AM**: Initial investigation focused on the application server logs, revealing a surge in database connection errors.
- **2:25 AM**: Network diagnostics were conducted due to an initial assumption of network latency issues, which proved misleading as no issues were found.
- **2:40 AM**: The incident was escalated to the database team after identifying the database as a potential cause.
- **3:00 AM**: Misleading debugging steps included restarting the database servers and clearing caches, neither of which resolved the issue.
- **3:30 AM**: The root cause was identified as a recent deployment bug that caused database connections to remain open indefinitely.
- **4:00 AM**: A hotfix was deployed to resolve the connection handling issue, and the database connection pool was reset.
- **4:30 AM**: The service was fully restored, and normal operations resumed.

## Root Cause and Resolution

The root cause of the outage was a code deployment that introduced a bug in the way database connections were handled. Specifically, the application failed to release connections back to the pool after use, leading to connection pool exhaustion.

**Resolution Steps**:
1. Rolled back the faulty deployment to the last stable version.
2. Deployed a hotfix to correct the connection handling code.
3. Reset the database connection pool to restore normal operations.

## Corrective and Preventative Measures

**Improvements and fixes**:
- **Code Review**: Implement stricter code reviews with a focus on connection handling to prevent similar issues.
- **Testing**: Introduce load testing scenarios in the CI/CD pipeline to catch potential issues with connection handling under high traffic.
- **Monitoring Enhancements**: Add alerts specifically for monitoring database connection pool metrics.

**Task List**:
- [ ] Patch the database driver to the latest version for improved connection management.
- [ ] Implement monitoring on database connection pool health.
- [ ] Refactor connection handling code to ensure proper release of connections after each transaction.
- [ ] Conduct a training session for the development team on effective database connection management.


