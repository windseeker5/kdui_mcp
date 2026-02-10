"""Design system configuration for KD UI Framework."""


def get_design_system() -> dict:
    """
    Get the complete design system configuration.
    
    This includes:
    - Color palette (primary, secondary, accent, neutral, semantic colors)
    - Typography scale (font sizes, weights, line heights)
    - Spacing system (margins, padding)
    - Border radius values
    - Shadow styles
    - Breakpoints for responsive design
    """
    return {
        "colors": {
            "primary": {
                "50": "#eff6ff",
                "100": "#dbeafe",
                "200": "#bfdbfe",
                "300": "#93c5fd",
                "400": "#60a5fa",
                "500": "#3b82f6",  # Main primary color
                "600": "#2563eb",
                "700": "#1d4ed8",
                "800": "#1e40af",
                "900": "#1e3a8a"
            },
            "secondary": {
                "50": "#f8fafc",
                "100": "#f1f5f9",
                "200": "#e2e8f0",
                "300": "#cbd5e1",
                "400": "#94a3b8",
                "500": "#64748b",  # Main secondary color
                "600": "#475569",
                "700": "#334155",
                "800": "#1e293b",
                "900": "#0f172a"
            },
            "accent": {
                "50": "#fdf4ff",
                "100": "#fae8ff",
                "200": "#f5d0fe",
                "300": "#f0abfc",
                "400": "#e879f9",
                "500": "#d946ef",  # Main accent color
                "600": "#c026d3",
                "700": "#a21caf",
                "800": "#86198f",
                "900": "#701a75"
            },
            "success": {
                "light": "#d1fae5",
                "main": "#10b981",
                "dark": "#047857"
            },
            "warning": {
                "light": "#fef3c7",
                "main": "#f59e0b",
                "dark": "#d97706"
            },
            "error": {
                "light": "#fee2e2",
                "main": "#ef4444",
                "dark": "#dc2626"
            },
            "info": {
                "light": "#dbeafe",
                "main": "#3b82f6",
                "dark": "#1d4ed8"
            },
            "neutral": {
                "white": "#ffffff",
                "50": "#fafafa",
                "100": "#f5f5f5",
                "200": "#e5e5e5",
                "300": "#d4d4d4",
                "400": "#a3a3a3",
                "500": "#737373",
                "600": "#525252",
                "700": "#404040",
                "800": "#262626",
                "900": "#171717",
                "black": "#000000"
            }
        },
        "typography": {
            "fontFamily": {
                "sans": "Inter, system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif",
                "mono": "'JetBrains Mono', 'Fira Code', 'Courier New', monospace"
            },
            "fontSize": {
                "xs": "0.75rem",      # 12px
                "sm": "0.875rem",     # 14px
                "base": "1rem",       # 16px
                "lg": "1.125rem",     # 18px
                "xl": "1.25rem",      # 20px
                "2xl": "1.5rem",      # 24px
                "3xl": "1.875rem",    # 30px
                "4xl": "2.25rem",     # 36px
                "5xl": "3rem",        # 48px
                "6xl": "3.75rem"      # 60px
            },
            "fontWeight": {
                "light": "300",
                "normal": "400",
                "medium": "500",
                "semibold": "600",
                "bold": "700",
                "extrabold": "800"
            },
            "lineHeight": {
                "none": "1",
                "tight": "1.25",
                "snug": "1.375",
                "normal": "1.5",
                "relaxed": "1.625",
                "loose": "2"
            }
        },
        "spacing": {
            "0": "0",
            "1": "0.25rem",    # 4px
            "2": "0.5rem",     # 8px
            "3": "0.75rem",    # 12px
            "4": "1rem",       # 16px
            "5": "1.25rem",    # 20px
            "6": "1.5rem",     # 24px
            "8": "2rem",       # 32px
            "10": "2.5rem",    # 40px
            "12": "3rem",      # 48px
            "16": "4rem",      # 64px
            "20": "5rem",      # 80px
            "24": "6rem"       # 96px
        },
        "borderRadius": {
            "none": "0",
            "sm": "0.125rem",   # 2px
            "base": "0.25rem",  # 4px
            "md": "0.375rem",   # 6px
            "lg": "0.5rem",     # 8px
            "xl": "0.75rem",    # 12px
            "2xl": "1rem",      # 16px
            "full": "9999px"
        },
        "shadows": {
            "sm": "0 1px 2px 0 rgba(0, 0, 0, 0.05)",
            "base": "0 1px 3px 0 rgba(0, 0, 0, 0.1), 0 1px 2px 0 rgba(0, 0, 0, 0.06)",
            "md": "0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06)",
            "lg": "0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -2px rgba(0, 0, 0, 0.05)",
            "xl": "0 20px 25px -5px rgba(0, 0, 0, 0.1), 0 10px 10px -5px rgba(0, 0, 0, 0.04)",
            "2xl": "0 25px 50px -12px rgba(0, 0, 0, 0.25)",
            "inner": "inset 0 2px 4px 0 rgba(0, 0, 0, 0.06)",
            "none": "none",
            # Shadcn-inspired shadows for enhanced polish
            "shadcn_card": "0 1px 3px rgba(0,0,0,0.12), 0 1px 2px rgba(0,0,0,0.24)",
            "shadcn_button": "inset 0 1px 0 rgba(255,255,255,0.1), 0 2px 4px rgba(0,0,0,0.2)",
            "shadcn_hover": "0 4px 8px rgba(0,0,0,0.15), 0 2px 4px rgba(0,0,0,0.1)"
        },
        "borders": {
            "subtle": "1px solid rgba(0, 0, 0, 0.05)",
            "light": "1px solid rgba(0, 0, 0, 0.1)",
            "normal": "1px solid rgba(0, 0, 0, 0.2)",
            "dark": "1px solid rgba(0, 0, 0, 0.3)"
        },
        "transitions": {
            "fast": "150ms cubic-bezier(0.4, 0, 0.2, 1)",
            "base": "200ms cubic-bezier(0.4, 0, 0.2, 1)",
            "slow": "300ms cubic-bezier(0.4, 0, 0.2, 1)",
            "smooth": "all 0.2s ease-in-out"
        },
        "breakpoints": {
            "sm": "640px",
            "md": "768px",
            "lg": "1024px",
            "xl": "1280px",
            "2xl": "1536px"
        },
        "daisyui_themes": {
            "light": {
                "primary": "#3b82f6",
                "secondary": "#64748b",
                "accent": "#d946ef",
                "neutral": "#262626",
                "base-100": "#ffffff",
                "base-200": "#f5f5f5",
                "base-300": "#e5e5e5",
                "info": "#3b82f6",
                "success": "#10b981",
                "warning": "#f59e0b",
                "error": "#ef4444"
            },
            "dark": {
                "primary": "#60a5fa",
                "secondary": "#94a3b8",
                "accent": "#e879f9",
                "neutral": "#171717",
                "base-100": "#1e293b",
                "base-200": "#0f172a",
                "base-300": "#020617",
                "info": "#60a5fa",
                "success": "#10b981",
                "warning": "#f59e0b",
                "error": "#ef4444"
            }
        },
        "component_defaults": {
            "card": {
                "padding": "1.5rem",
                "borderRadius": "0.5rem",
                "shadow": "md"
            },
            "button": {
                "paddingX": "1rem",
                "paddingY": "0.5rem",
                "borderRadius": "0.375rem",
                "fontSize": "0.875rem",
                "fontWeight": "500"
            },
            "input": {
                "paddingX": "0.75rem",
                "paddingY": "0.5rem",
                "borderRadius": "0.375rem",
                "fontSize": "0.875rem",
                "borderWidth": "1px"
            },
            "table": {
                "headerBg": "#f5f5f5",
                "stripedBg": "#fafafa",
                "borderColor": "#e5e5e5",
                "hoverBg": "#f0f9ff"
            }
        },
        "best_practices": {
            "contrast": {
                "description": "Maintain WCAG AA contrast ratio of at least 4.5:1 for normal text",
                "primary_on_white": "✅ Pass",
                "secondary_on_white": "✅ Pass"
            },
            "spacing": {
                "description": "Use consistent spacing scale (4px base)",
                "between_components": "spacing.6 (24px)",
                "within_components": "spacing.4 (16px)",
                "tight_spacing": "spacing.2 (8px)"
            },
            "hierarchy": {
                "description": "Establish clear visual hierarchy",
                "h1": "fontSize.4xl + fontWeight.bold",
                "h2": "fontSize.3xl + fontWeight.bold",
                "h3": "fontSize.2xl + fontWeight.semibold",
                "body": "fontSize.base + fontWeight.normal"
            }
        }
    }
