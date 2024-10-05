# """Welcome to Reflex! This file outlines the steps to create a basic app."""
#
import reflex as rx
#
from rxconfig import config


#
#
class State(rx.State):
    """The app state."""

    ...


# def index() -> rx.Component:
#     # Welcome Page (Index)
#     return rx.container(
#         rx.color_mode.button(position="top-right"),
#         rx.vstack(
#             rx.heading("Welcome to Reflex!", size="9"),
#             rx.text(
#                 "Get started by editing ",
#                 rx.code(f"{config.app_name}/{config.app_name}.py"),
#                 size="5",
#             ),
#             rx.link(
#                 rx.button("Check out our docs!"),
#                 href="https://reflex.dev/docs/getting-started/introduction/",
#                 is_external=True,
#             ),
#             spacing="5",
#             justify="center",
#             min_height="85vh",
#         ),
#         rx.logo(),
#     )
#
def create_nav_link(text):
    """Create a navigation link with custom styling."""
    return rx.el.a(
        text,
        class_name="dark:hover:text-[#7faf7f] dark:text-gray-200 hover:text-[#a0c8a0]",
        href="#",
        font_weight="600",
        color="#ffffff",
        font_size="1.25rem",
        line_height="1.75rem",
    )


def create_nav_list_item(text):
    """Create a list item containing a navigation link."""
    return rx.el.li(create_nav_link(text=text))


def create_icon(alt_text, class_name, display, icon_tag):
    """Create an icon with specified properties."""
    return rx.icon(
        alt=alt_text,
        class_name=class_name,
        tag=icon_tag,
        display=display,
        height="2rem",
        width="2rem",
    )


def create_section_heading(margin_bottom, text):
    """Create a section heading with custom styling and margin."""
    return rx.heading(
        text,
        class_name="dark:text-[#7faf7f] text-[#588658]",
        font_weight="700",
        margin_bottom=margin_bottom,
        font_size="2.25rem",
        line_height="2.5rem",
        text_align="center",
        as_="h2",
    )


def create_subsection_heading(text):
    """Create a subsection heading with custom styling."""
    return rx.heading(
        text,
        class_name="dark:text-[#7faf7f] text-[#588658]",
        font_weight="600",
        margin_bottom="1rem",
        font_size="1.5rem",
        line_height="2rem",
        as_="h3",
    )


def create_paragraph(text):
    """Create a paragraph with custom styling."""
    return rx.text(
        text,
        class_name="dark:text-gray-200",
        line_height="1.75rem",
        color="#1F2937",
        font_size="1.125rem",
    )


def create_feature_box(title, description):
    """Create a feature box with a title and description."""
    return rx.box(
        create_subsection_heading(text=title),
        create_paragraph(text=description),
        class_name="dark:bg-gray-900",
        background_color="#ffffff",
        padding="2rem",
        border_radius="1rem",
        box_shadow="0 20px 25px -5px rgba(0, 0, 0, 0.1), 0 10px 10px -5px rgba(0, 0, 0, 0.04)",
    )


def create_testimonial_text(text):
    """Create styled text for a testimonial."""
    return rx.text(
        text,
        class_name="dark:text-gray-200",
        line_height="1.75rem",
        margin_bottom="1.5rem",
        color="#1F2937",
        font_size="1.25rem",
    )


def create_testimonial_author(author):
    """Create styled text for a testimonial author."""
    return rx.text(
        author,
        class_name="dark:text-[#7faf7f] text-[#588658]",
        font_weight="700",
        font_size="1.125rem",
        line_height="1.75rem",
    )


def create_testimonial_box(quote, author):
    """Create a testimonial box with a quote and author."""
    return rx.box(
        create_testimonial_text(text=quote),
        create_testimonial_author(author=author),
        class_name="dark:bg-gray-900",
        background_color="#ffffff",
        padding="2rem",
        border_radius="1rem",
        box_shadow="0 20px 25px -5px rgba(0, 0, 0, 0.1), 0 10px 10px -5px rgba(0, 0, 0, 0.04)",
    )


def create_form_label(label_text):
    """Create a form label with custom styling."""
    return rx.el.label(
        label_text,
        class_name="dark:text-gray-200",
        display="block",
        font_weight="700",
        margin_bottom="0.75rem",
        color="#1F2937",
        font_size="1.25rem",
        line_height="1.75rem",
    )


def create_form_input(input_id, input_name, input_type):
    """Create a form input field with custom styling."""
    return rx.el.input(
        class_name="border-[#588658] dark:bg-gray-800 dark:border-[#7faf7f] dark:focus:ring-[#7faf7f] dark:text-gray-200 focus:ring-[#588658]",
        id=input_id,
        name=input_name,
        type=input_type,
        background_color="#F3F4F6",
        border_width="2px",
        _focus={
            "outline-style": "none",
            "box-shadow": "var(--tw-ring-inset) 0 0 0 calc(2px + var(--tw-ring-offset-width)) var(--tw-ring-color)",
        },
        padding_left="1rem",
        padding_right="1rem",
        padding_top="0.75rem",
        padding_bottom="0.75rem",
        border_radius="0.5rem",
        color="#1F2937",
        font_size="1.125rem",
        line_height="1.75rem",
        width="100%",
    )


def create_form_field(
        label_text, input_id, input_name, input_type
):
    """Create a form field with label and input."""
    return rx.box(
        create_form_label(label_text=label_text),
        create_form_input(
            input_id=input_id,
            input_name=input_name,
            input_type=input_type,
        ),
        margin_bottom="1.5rem",
    )


def create_social_icon(alt_text, icon_tag):
    """Create a social media icon."""
    return rx.icon(
        alt=alt_text,
        tag=icon_tag,
        height="2rem",
        width="2rem",
    )


def create_social_link(alt_text, icon_tag):
    """Create a social media link with an icon."""
    return rx.el.a(
        create_social_icon(
            alt_text=alt_text, icon_tag=icon_tag
        ),
        class_name="dark:hover:text-[#7faf7f] hover:text-[#a0c8a0]",
        href="#",
    )


def create_navigation():
    """Create the main navigation component with links and dark mode toggle."""
    return rx.flex(
        rx.list(
            create_nav_list_item(text="Home"),
            create_nav_list_item(text="Products"),
            create_nav_list_item(text="About"),
            display="flex",
            column_gap="2rem",
        ),
        rx.el.button(
            create_icon(
                alt_text="Light mode",
                class_name="dark:hidden",
                display="block",
                icon_tag="sun",
            ),
            create_icon(
                alt_text="Dark mode",
                class_name="dark:block",
                display="none",
                icon_tag="moon",
            ),
            class_name="bg-[#a0c8a0] dark:bg-[#4a6b4a]",
            id="darkModeToggle",
            margin_left="2rem",
            padding="0.75rem",
            border_radius="9999px",
        ),
        display="flex",
        align_items="center",
    )


def create_header():
    """Create the header component with logo and navigation."""
    return rx.flex(
        rx.heading(
            "Heidelbell",
            class_name="dark:text-gray-200",
            font_weight="800",
            font_size="2.25rem",
            line_height="2.5rem",
            color="#ffffff",
            as_="h1",
        ),
        create_navigation(),
        width="100%",
        style=rx.breakpoints(
            {
                "640px": {"max-width": "640px"},
                "768px": {"max-width": "768px"},
                "1024px": {"max-width": "1024px"},
                "1280px": {"max-width": "1280px"},
                "1536px": {"max-width": "1536px"},
            }
        ),
        display="flex",
        align_items="center",
        justify_content="space-between",
        margin_left="auto",
        margin_right="auto",
        padding_left="1.5rem",
        padding_right="1.5rem",
        padding_top="2rem",
        padding_bottom="2rem",
    )


def create_cta_button():
    """Create a call-to-action button."""
    return rx.el.a(
        "Learn More",
        class_name="dark:bg-gray-800 dark:hover:bg-[#4a6b4a] dark:text-[#7faf7f] hover:bg-[#a0c8a0] text-[#588658]",
        href="#",
        background_color="#ffffff",
        transition_duration="300ms",
        font_weight="700",
        padding_left="2.5rem",
        padding_right="2.5rem",
        padding_top="1rem",
        padding_bottom="1rem",
        border_radius="9999px",
        font_size="1.25rem",
        line_height="1.75rem",
        transition_property="background-color, border-color, color, fill, stroke, opacity, box-shadow, transform",
        transition_timing_function="cubic-bezier(0.4, 0, 0.2, 1)",
    )


def create_hero_content():
    """Create the content for the hero section."""
    return rx.box(
        rx.heading(
            "Innovating for Tomorrow",
            font_weight="700",
            margin_bottom="2rem",
            font_size="3rem",
            line_height="1",
            as_="h2",
        ),
        rx.text(
            "Creating cutting-edge solutions that transform industries.",
            line_height="2rem",
            margin_bottom="2.5rem",
            font_size="1.5rem",
        ),
        create_cta_button(),
        width="100%",
        style=rx.breakpoints(
            {
                "640px": {"max-width": "640px"},
                "768px": {"max-width": "768px"},
                "1024px": {"max-width": "1024px"},
                "1280px": {"max-width": "1280px"},
                "1536px": {"max-width": "1536px"},
            }
        ),
        margin_left="auto",
        margin_right="auto",
        padding_left="1.5rem",
        padding_right="1.5rem",
        position="relative",
        text_align="center",
        z_index="10",
    )


def create_hero_section():
    """Create the hero section with background, content, and animated elements."""
    return rx.box(
        rx.box(
            class_name="parallax",
            background_image="url('https://images.pexels.com/photos/4737484/pexels-photo-4737484.jpeg')",
            position="absolute",
            top="0",
            right="0",
            bottom="0",
            left="0",
            opacity="0.2",
        ),
        create_hero_content(),
        rx.box(
            class_name="animate-[pulse_3s_ease-in-out_infinite]",
            position="absolute",
            background_color="#ffffff",
            height="6rem",
            left="25%",
            opacity="0.5",
            border_radius="9999px",
            top="25%",
            width="6rem",
        ),
        rx.box(
            class_name="animate-[pulse_4s_ease-in-out_infinite]",
            position="absolute",
            background_color="#ffffff",
            height="8rem",
            opacity="0.3",
            right="25%",
            border_radius="9999px",
            top="50%",
            width="8rem",
        ),
        rx.box(
            class_name="animate-[pulse_5s_ease-in-out_infinite] left-1/3",
            position="absolute",
            background_color="#ffffff",
            bottom="25%",
            height="7rem",
            opacity="0.4",
            border_radius="9999px",
            width="7rem",
        ),
        rx.image(
            alt="Innovation Icon",
            class_name="animate-[float_6s_ease-in-out_infinite]",
            src="https://reflex-hosting-dev-flexgen.s3.us-west-2.amazonaws.com/replicate/NNTh4x4VdmJQE1diG9G8sBMD3qLmE6mBjs9r0TQcUzvOIj3E/out-0.webp",
            position="absolute",
            bottom="4rem",
            height="8rem",
            right="4rem",
            width="8rem",
        ),
        class_name="bg-[#588658] dark:bg-[#3d5e3d]",
        overflow="hidden",
        padding_top="6rem",
        padding_bottom="6rem",
        position="relative",
        color="#ffffff",
    )


def create_products_section():
    """Create the products section with feature boxes."""
    return rx.box(
        create_section_heading(
            margin_bottom="4rem", text="Our Products"
        ),
        rx.box(
            create_feature_box(
                title="Analytics Platform",
                description="Harness the power of data with our analytics solution.",
            ),
            create_feature_box(
                title="IoT Devices",
                description="Connect and control your world with our IoT ecosystem.",
            ),
            create_feature_box(
                title="AI Assistants",
                description="Experience the future with intelligent digital assistants.",
            ),
            gap="3rem",
            display="grid",
            grid_template_columns=rx.breakpoints(
                {
                    "0px": "repeat(1, minmax(0, 1fr))",
                    "768px": "repeat(3, minmax(0, 1fr))",
                }
            ),
        ),
        width="100%",
        style=rx.breakpoints(
            {
                "640px": {"max-width": "640px"},
                "768px": {"max-width": "768px"},
                "1024px": {"max-width": "1024px"},
                "1280px": {"max-width": "1280px"},
                "1536px": {"max-width": "1536px"},
            }
        ),
        margin_left="auto",
        margin_right="auto",
        padding_left="1.5rem",
        padding_right="1.5rem",
    )


def create_testimonials_section():
    """Create the testimonials section with customer quotes."""
    return rx.box(
        rx.heading(
            "Customer Testimonials",
            class_name="dark:text-white",
            font_weight="700",
            margin_bottom="4rem",
            font_size="2.25rem",
            line_height="2.5rem",
            text_align="center",
            color="#1F2937",
            as_="h2",
        ),
        rx.box(
            create_testimonial_box(
                quote='"Heidelbell\'s products have revolutionized our business processes."',
                author="John Doe, TechCorp",
            ),
            create_testimonial_box(
                quote='"Outstanding customer support, ensuring smooth operations 24/7."',
                author="Jane Smith, InnovateCo",
            ),
            gap="3rem",
            display="grid",
            grid_template_columns=rx.breakpoints(
                {
                    "0px": "repeat(1, minmax(0, 1fr))",
                    "768px": "repeat(2, minmax(0, 1fr))",
                }
            ),
        ),
        width="100%",
        style=rx.breakpoints(
            {
                "640px": {"max-width": "640px"},
                "768px": {"max-width": "768px"},
                "1024px": {"max-width": "1024px"},
                "1280px": {"max-width": "1280px"},
                "1536px": {"max-width": "1536px"},
            }
        ),
        margin_left="auto",
        margin_right="auto",
        padding_left="1.5rem",
        padding_right="1.5rem",
    )


def create_message_textarea():
    """Create a textarea for the contact form message."""
    return rx.el.textarea(
        class_name="border-[#588658] dark:bg-gray-800 dark:border-[#7faf7f] dark:focus:ring-[#7faf7f] dark:text-gray-200 focus:ring-[#588658]",
        id="message",
        name="message",
        rows="6",
        background_color="#F3F4F6",
        border_width="2px",
        _focus={
            "outline-style": "none",
            "box-shadow": "var(--tw-ring-inset) 0 0 0 calc(2px + var(--tw-ring-offset-width)) var(--tw-ring-color)",
        },
        padding_left="1rem",
        padding_right="1rem",
        padding_top="0.75rem",
        padding_bottom="0.75rem",
        border_radius="0.5rem",
        color="#1F2937",
        font_size="1.125rem",
        line_height="1.75rem",
        width="100%",
    )


def create_submit_button():
    """Create a submit button for the contact form."""
    return rx.el.button(
        "Send",
        class_name="bg-[#588658] dark:bg-[#4a6b4a] dark:hover:bg-[#3d5e3d] hover:bg-[#4a6b4a]",
        type="submit",
        transition_duration="300ms",
        font_weight="700",
        padding_left="1.5rem",
        padding_right="1.5rem",
        padding_top="1rem",
        padding_bottom="1rem",
        border_radius="0.5rem",
        color="#ffffff",
        font_size="1.25rem",
        line_height="1.75rem",
        transition_property="background-color, border-color, color, fill, stroke, opacity, box-shadow, transform",
        transition_timing_function="cubic-bezier(0.4, 0, 0.2, 1)",
        width="100%",
    )


def create_contact_form():
    """Create the contact form with input fields and submit button."""
    return rx.form(
        create_form_field(
            label_text="Name",
            input_id="name",
            input_name="name",
            input_type="text",
        ),
        create_form_field(
            label_text="Email",
            input_id="email",
            input_name="email",
            input_type="email",
        ),
        rx.box(
            create_form_label(label_text="Message"),
            create_message_textarea(),
            margin_bottom="1.5rem",
        ),
        create_submit_button(),
        class_name="dark:bg-gray-900",
        background_color="#ffffff",
        padding="2.5rem",
        border_radius="1rem",
        box_shadow="0 20px 25px -5px rgba(0, 0, 0, 0.1), 0 10px 10px -5px rgba(0, 0, 0, 0.04)",
    )


def create_contact_section():
    """Create the contact section with heading and form."""
    return rx.box(
        rx.box(
            create_section_heading(
                margin_bottom="3rem", text="Contact Us"
            ),
            create_contact_form(),
            max_width="36rem",
            margin_left="auto",
            margin_right="auto",
            padding_left="1.5rem",
            padding_right="1.5rem",
        ),
        class_name="dark:bg-gray-800",
        background_color="#F3F4F6",
        padding_top="5rem",
        padding_bottom="5rem",
    )


def create_main_content():
    """Create the main content sections of the page."""
    return rx.box(
        create_hero_section(),
        rx.box(
            create_products_section(),
            class_name="dark:bg-gray-800",
            background_color="#F3F4F6",
            padding_top="5rem",
            padding_bottom="5rem",
        ),
        rx.box(
            create_testimonials_section(),
            class_name="bg-[#a0c8a0] dark:bg-[#4a6b4a]",
            padding_top="5rem",
            padding_bottom="5rem",
        ),
        create_contact_section(),
    )


def create_footer_content():
    """Create the main content for the footer."""
    return rx.flex(
        rx.box(
            rx.heading(
                "Heidelbell",
                font_weight="700",
                font_size="1.875rem",
                line_height="2.25rem",
                as_="h3",
            ),
            margin_bottom=rx.breakpoints(
                {"0px": "1.5rem", "768px": "0"}
            ),
            width=rx.breakpoints(
                {"0px": "100%", "768px": "auto"}
            ),
        ),
        rx.box(
            rx.flex(
                create_social_link(
                    alt_text="Facebook", icon_tag="facebook"
                ),
                create_social_link(
                    alt_text="Twitter", icon_tag="twitter"
                ),
                create_social_link(
                    alt_text="LinkedIn", icon_tag="linkedin"
                ),
                display="flex",
                column_gap="1.5rem",
            ),
            width=rx.breakpoints(
                {"0px": "100%", "768px": "auto"}
            ),
        ),
        display="flex",
        flex_wrap="wrap",
        align_items="center",
        justify_content="space-between",
    )


def create_footer():
    """Create the footer section with content and copyright notice."""
    return rx.box(
        create_footer_content(),
        rx.box(
            rx.text(
                "© 2023 Heidelbell. All rights reserved."
            ),
            margin_top="2rem",
            text_align="center",
            font_size="1.125rem",
            line_height="1.75rem",
        ),
        width="100%",
        style=rx.breakpoints(
            {
                "640px": {"max-width": "640px"},
                "768px": {"max-width": "768px"},
                "1024px": {"max-width": "1024px"},
                "1280px": {"max-width": "1280px"},
                "1536px": {"max-width": "1536px"},
            }
        ),
        margin_left="auto",
        margin_right="auto",
        padding_left="1.5rem",
        padding_right="1.5rem",
    )


def create_page_layout():
    """Create the overall page layout including header, main content, and footer."""
    return rx.box(
        rx.box(
            create_header(),
            class_name="bg-[#588658] dark:bg-[#3d5e3d]",
            box_shadow="0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -2px rgba(0, 0, 0, 0.05)",
        ),
        create_main_content(),
        rx.box(
            create_footer(),
            class_name="bg-[#4a6b4a] dark:bg-[#3d5e3d]",
            padding_top="3rem",
            padding_bottom="3rem",
            color="#ffffff",
        ),
        min_height="100vh",
    )


def create_page():
    """Create the complete page with styles, scripts, and layout."""
    return rx.fragment(
        rx.script(src="https://cdn.tailwindcss.com"),
        rx.el.style(
            """
        @font-face {
            font-family: 'LucideIcons';
            src: url(https://unpkg.com/lucide-static@latest/font/Lucide.ttf) format('truetype');
        }

        @keyframes float {
            0% { transform: translateY(0px); }
            50% { transform: translateY(-20px); }
            100% { transform: translateY(0px); }
        }

        @keyframes pulse {
            0% { opacity: 0.6; }
            50% { opacity: 1; }
            100% { opacity: 0.6; }
        }

        .parallax {
            background-attachment: sticky;
            background-position: center;
            background-repeat: no-repeat;
            background-size: cover;
        }
    """
        ),
        rx.box(
            create_page_layout(),
            rx.script(
                """
    const darkModeToggle = document.getElementById('darkModeToggle');
    const htmlElement = document.documentElement;

    darkModeToggle.addEventListener('click', () => {
        htmlElement.classList.toggle('dark');
    });

    if (window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches) {
        htmlElement.classList.add('dark');
    }
"""
            ),
            class_name="dark:bg-gray-900",
            background_color="#ffffff",
            transition_duration="300ms",
            transition_property="color, background-color, border-color, text-decoration-color, fill, stroke",
            transition_timing_function="cubic-bezier(0.4, 0, 0.2, 1)",
        ),
    )


app = rx.App()
# app.add_page(create_nav_link)
