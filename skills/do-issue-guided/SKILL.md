---
name: do-issue-guided
description: Work on a GitHub issue end-to-end with human approval gates at design and plan phases. Request additional information and chat with user for solution development and implementation.
argument-hint: issue number (e.g., 123)
disable-model-invocation: true
user-invocable: true
---

**Depends on:** scope-boundaries, git-workflow, github-issue-workflow, create-solution-design, create-implementation-plan, plan-execution, local-verification, cicd-bestpractice, claude-code-recovery, logging-bestpractice, alerting-bestpractice, systematic-debugging, pullrequest-review

# Work on GitHub Issue (Guided)

Work on GitHub issue `$ARGUMENTS` with human approval gates before implementation begins. Follow every phase in order. Do not skip phases.

## Phase 1-2: Understand the Issue and Solution Design (subagent)

Run Phases 1 and 2 as a subagent to keep the main context window clean for implementation.

1. Initialise the issue state file per the github-issue-workflow skill.
2. Dispatch the **issue-analyst** agent with:
   - Issue number: `$ARGUMENTS`
   - Mode: `guided`
3. When the agent returns, verify:
   - `.claude/issue-state.json` has `phase` set to `design`
   - `.claude/issue-state.json` has `comments.design` set to a comment ID
4. If the agent flagged ambiguities, ask the user clarifying questions before proceeding.
5. **Present the design to the user for review. Do not proceed until approved.**
6. If the user requests changes, re-dispatch the **issue-analyst** agent with the revision context and repeat from step 3.

## Phase 3: Implementation Plan (subagent)

Run Phase 3 as a subagent to keep the main context window clean for implementation.

1. Dispatch the **issue-planner** agent with:
   - Issue number: `$ARGUMENTS`
   - Design comment ID from `.claude/issue-state.json`
2. When the agent returns, verify:
   - `.claude/issue-state.json` has `phase` set to `plan`
   - `.claude/issue-state.json` has `comments.plan` set to a comment ID
3. **Present the plan to the user for approval. Do not proceed until approved.**
4. If the user requests changes, re-dispatch the **issue-planner** agent with the revision context and repeat from step 2.

## Phase 4: Create Branch

1. Derive the branch name per the github-issue-workflow skill (branching conventions).
2. Create the branch from the project's integration branch (typically `develop`).
3. Confirm the branch name to the user.
4. Update phase to `branch` in the state file.

## Phase 5: Execute the Plan

1. Follow the plan-execution skill to execute each step.
2. The plan-execution skill handles: step-by-step implementation, verification, failure handling, progress tracking, crash recovery, and acceptance criteria checking.
3. In guided mode, it will provide checkpoints and pause when uncertain.
4. Update phase to `implement` in the state file.

## Phase 6: Code Review

1. Dispatch the code-reviewer agent with the issue requirements and the diff (`git diff develop...HEAD`).
2. The reviewer performs two-stage review: spec compliance first, then code quality.
3. If spec compliance fails, stop — fix the gaps before requesting re-review.
4. Process code quality feedback per the pullrequest-review skill:
   - Read all items before acting.
   - Clarify unclear items before implementing any.
   - Verify each suggestion against the codebase.
   - Push back with reasoning when a suggestion is incorrect.
   - Implement valid fixes one at a time, verifying after each.
5. If fixes changed the implementation approach, update the plan comment on the issue.
6. Request re-review if there were critical or spec compliance issues. Repeat until approved.
7. Update phase to `review` in the state file.

## Phase 7: Push and Verify CI

1. Run pre-push verification per the local-verification skill (lint, typecheck, tests). Fix any failures before pushing.
2. Push the branch to remote.
3. Monitor CI status per the cicd-bestpractice skill. If CI fails, read the failure logs, fix locally, and push again. Do not proceed until CI passes.

## Phase 8: Update Issue and Create PR

1. Post a completion comment on the issue per the github-issue-workflow skill (post completion comment pattern).
2. Ask the user if they want to:
   - Create a pull request (using the github-issue-workflow PR pattern)
   - Just keep the branch as-is (already pushed)
   - Do nothing further
3. Update phase to `complete` in the state file.
4. Clean up the state file after PR creation (if applicable).

## Rules

- **Always pause for user approval** after presenting the design (Phase 2) and the plan (Phase 3).
- **Run verification** after each step and after all steps. Do not declare success if checks fail.
- **Do not push or create PRs** unless explicitly asked by the user.
- **Never commit directly** to `main` or `develop`.
- **Use conventional commits** that reference the issue number (e.g., `feat: add rubric export (#42)`).
