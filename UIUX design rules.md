Here is a comprehensive set of UI/UX design rules, constraints, and logic derived from your video sources.

This text is structured as a **System Prompt / Configuration Document** suitable for fine-tuning or instructing your MCP server. It categorizes instructions into Dashboard Logic, Visual Systems, and Common Mistakes to ensure your AI generates standardized, aesthetic, and functional interfaces.

***

# UI/UX Design Standards & Logic for MCP Server

## 1. Dashboard Architecture & Layout Logic
*Use these rules when the user request involves "Dashboards," "Admin Panels," or "Data Visualization."*

*   **Navigation Models:**
    *   **Split Navigation:** Do not use a single menu for everything. Place global actions (User Profile, Settings, Logout) in a **Top Bar**. Place context-specific views (Data Types, Views) in a **Left Sidebar** (The "Spine").
    *   **Sidebar Hierarchy:** Group links by relevance. Place high-frequency links at the top; place "Settings" or "Help" at the bottom. Use collapsible menus for depth to reduce cognitive load.
    *   **Breadcrumbs:** Always implement breadcrumbs for deep content flows to maintain user context.
*   **Information Density & Grid:**
    *   **Dashboard vs. Landing Page:** Dashboards require higher information density. Use smaller font sizes and stricter grids than marketing pages.
    *   **Compact Spacing:** Avoid excess padding and whitespace in data-heavy views. Data must be available with the least amount of scrolling.
    *   **Grid Structure:** Use a strict grid (e.g., 2-column or 3-column) to organize widgets. Place the most critical metrics or actions (e.g., Project Status, Financial Totals) at the very top left or center.
*   **Dynamic Content:**
    *   Prioritize dynamic, changing data. Do not dedicate prime screen real estate to static content that does not change.

## 2. Visual Style System (The "Look & Feel")
*Apply these rules to normalize the aesthetics of generated web pages and components.*

*   **Typography Rules:**
    *   **Font Limit:** Use a maximum of 2 fonts. (Recommendation: 1 for Headings, 1 for Body, or 1 font family with different weights).
    *   **Hierarchy Scale:**
        *   **H1:** Hero sections/Page Titles.
        *   **H2:** Section Headings.
        *   **H3/Body Large:** Subcategories.
        *   **Body Small:** Details/Metadata.
    *   **Readability:** Ensure text containers do not exceed **600px** in width to maintain optimal reading experience.
*   **Relationship-Based Spacing (The Multiplier Rule):**
    *   Define spacing based on element relationships.
    *   *Rule:* If elements are related (e.g., Header + Body), use space `X` (e.g., 16px). If elements are distinct (e.g., Text Group + Button), use space `2X` (e.g., 32px).
    *   **Section Spacing:** For general web pages, use large vertical gaps (80px–160px) between major sections to create "breathing room".
*   **Color System:**
    *   **The 3-Color Rule:** Limit the palette to:
        1.  **Base:** Background color.
        2.  **Primary:** Call-to-Action (CTA) and accents.
        3.  **Neutral:** Text (Dark or Light).
    *   **Text Hierarchy via Opacity:** Instead of different gray hex codes, use the Neutral color with opacity:
        *   Primary Text: 100% or 80% opacity.
        *   Secondary Text: 60-70% opacity.
*   **Visual Polish:**
    *   **Banish "Flat" Design:** Add subtle inner shadows (white, low opacity) and drop shadows to buttons to make them tactile. Add subtle borders (5% opacity) to cards to define structure.
    *   **Break the Monotony:** While adhering to grids, occasionally break the layout with overflowing carousels or centered text to maintain visual interest.

## 3. Component & Interaction Logic
*Standardized rules for specific UI elements.*

*   **Charts & Data Visualization:**
    *   **Intent Matching:**
        *   Use **Bar Charts** for comparing data points.
        *   Use **Line Graphs** for plotting trends over time.
    *   **Simplicity:** Always include grid lines, clear axis numbers, and a summary/total at the top of the chart.
*   **Tables vs. Lists:**
    *   Use **Lists** for simple data (visual separation via spacing or dividers).
    *   Use **Tables** when functionality is required. Tables *must* include Search, Filter, and Sort capabilities.
*   **Modals vs. Popovers vs. Toasts:**
    *   **Popover:** Use for simple, non-blocking context (e.g., display settings) where the user can click away.
    *   **Modal:** Use for complex, blocking actions that require focus (e.g., creating a new item).
    *   **Toast:** Use for system feedback (success/error messages) that does not require user action.
*   **Empty States:**
    *   Always design an "Empty State" for lists/dashboards when no data exists yet. Do not leave a blank white space.

## 4. The "Anti-Patterns" (Mistakes to Avoid)
*Hard constraints: The Server must REJECT these patterns.*

1.  **Navigation Overload:** Do not cram all navigation links into a single sidebar or top menu. Segregate global vs. local nav.
2.  **Mental Model Mismatch:** Do not categorize menu items based on database structure; categorize them based on user workflow (User Research/Card Sorting logic).
3.  **Static Dashboarding:** Do not build dashboards that look like static web pages. If the content doesn't change, it doesn't belong on a dashboard.
4.  **Inconsistent Visuals:** Do not use raw colors without a defined palette. Do not mix more than 2 font families.
5.  **Lorem Ipsum Dependence:** Where possible, generate realistic content for the UI to test real-world text wrapping and layout, rather than relying solely on Lorem Ipsum.

***

### Suggested System Instruction for your MCP Server:
*"You are a UI Design Engine. When generating code or layouts, you must strictly adhere to the 'Dashboard Architecture' for application interfaces and 'Visual Style System' for general pages. You will reject requests to create 'flat' unstyled buttons, enforcing the 3-color rule and opacity-based hierarchy. For data inputs, you will automatically select the appropriate visualization (Bar vs Line) based on the data context."*