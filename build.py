import os
import time

#Setup paths
REVIEWS_DIR = 'reviews'
TEMPLATE_FILE = 'htmls/template.html'
REVIEW_LIST_OUTPUT = 'htmls/movies.html'
REVIEW_TEMPLATE = "htmls/review.html"
PLACEHOLDER = "***"
TITLE_PLACEHOLDER = "~~~"

#Creates the HTML string for a single card
def generate_html_card(title, color, content, path_to_file):
    path_to_file = path_to_file.replace("htmls/", "")
    return f"""
        <article class="movie-card">
          <div class="card-image" style="background-color: {color}"></div>
          <div class="card-content">
            <h2>{title}</h2>
            <p>{content}</p>
            <a href="{path_to_file}" class="read-more">Read Review &rarr;</a>
          </div>
        </article>
    """

def generate_review_html(title, content):
    return f"""
        <p>{content}</p>
    """

def make_path_safe(path):
    replacements = str.maketrans({
        " ": "_",
        "*": "",
        "?": "",
        "[": "",
        "]": "",
        "(": "",
        ")": "",
        "$": "",
        "&": "",
        ";": "",
        "|": "",
        "<": "",
        ">": "",
        "\\": "",
        "#": "",
    })
    return path.translate(replacements)

def main():
    print("🎬 Starting website build...")
    
    #Read the templates
    with open(TEMPLATE_FILE, 'r') as f:
        template_content = f.read()

    with open(REVIEW_TEMPLATE, 'r') as f:
        review_template = f.read()

    cards_html = ""
    review_html = ""

    files = os.listdir(REVIEWS_DIR)
    #sort files by the time they were last edited
    files.sort(key=lambda item:os.path.getmtime(os.path.join("reviews", item)))

    for filename in files:
        if filename.endswith(".txt"):
            filepath = os.path.join(REVIEWS_DIR, filename)
            
            with open(filepath, 'r') as f:
                lines = f.readlines()
                
                # Parse the file based on rules
                if len(lines) >= 3:
                    title = lines[0].strip()
                    color = lines[1].strip()
                    # Join the rest of the lines as the review body
                    body = "".join(lines[2:3]).strip()
                    review_text = "".join(lines[2:]).strip()
                    
                    # Generate the HTML for this specific movie
                    title_path = make_path_safe(title)
                    review_path = "htmls/reviews/" + title_path + ".html"
                    cards_html += generate_html_card(title, color, body, review_path)

                    # Generate HTML for this review's page
                    review_html += generate_review_html(title, review_text)
                    final_review_html = review_template.replace(TITLE_PLACEHOLDER, title)
                    final_review_html = final_review_html.replace(PLACEHOLDER, review_html)

                    
                    with open(review_path, 'w') as f:
                        f.write(final_review_html)
                    
                    print(f"   + Processed: {title}")

    #Inject cards into the template
    final_html = template_content.replace(PLACEHOLDER, cards_html)

    

    #Write the final movies.html file
    with open(REVIEW_LIST_OUTPUT, 'w') as f:
        f.write(final_html)

    print(f"✅ Success! {REVIEW_LIST_OUTPUT} has been generated.")

if __name__ == "__main__":
    main()