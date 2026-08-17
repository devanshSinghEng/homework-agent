import sqlite3
import matplotlib.pyplot as plt

def show_analytics():
    conn = sqlite3.connect("homework_tracker.db")
    cursor = conn.cursor()

    print("\n===== Homework Generation Analytics =====\n")

    cursor.execute("SELECT COUNT(*) FROM homework_log")
    total_sheets = cursor.fetchone()[0]
    print(f"Total homework sheets generated: {total_sheets}")

    cursor.execute("SELECT SUM(num_questions) FROM homework_log")
    total_questions = cursor.fetchone()[0] or 0
    print(f"Total questions generated: {total_questions}")

    print("\n--- Topic-wise breakdown ---")
    cursor.execute("""
        SELECT topic, COUNT(*) as sheet_count, SUM(num_questions) as question_count
        FROM homework_log
        GROUP BY topic
        ORDER BY sheet_count DESC
    """)
    rows = cursor.fetchall()
    for row in rows:
        topic, sheet_count, question_count = row
        print(f"{topic}: {sheet_count} sheet(s), {question_count} question(s)")

    print("\n--- Recent activity ---")
    cursor.execute("""
        SELECT source_pdf, topic, generated_on
        FROM homework_log
        ORDER BY generated_on DESC
        LIMIT 5
    """)
    recent = cursor.fetchall()
    for r in recent:
        print(f"{r[2]} | {r[0]} | Topic: {r[1]}")

    conn.close()


def plot_topic_chart():
    conn = sqlite3.connect("homework_tracker.db")
    cursor = conn.cursor()
    cursor.execute("""
        SELECT topic, COUNT(*) as sheet_count
        FROM homework_log
        GROUP BY topic
        ORDER BY sheet_count DESC
    """)
    rows = cursor.fetchall()
    conn.close()

    if not rows:
        print("Chart banane ke liye abhi data nahi hai.")
        return

    topics = [row[0] for row in rows]
    counts = [row[1] for row in rows]

    plt.figure(figsize=(8, 5))
    plt.bar(topics, counts, color="#5382A1")
    plt.xlabel("Topic")
    plt.ylabel("Homework Sheets Generated")
    plt.title("Homework Sheets by Topic")
    plt.xticks(rotation=30, ha="right")
    plt.tight_layout()
    plt.savefig("topic_chart.png")
    print("\nChart 'topic_chart.png' mein save ho gaya!")


if __name__ == "__main__":
    show_analytics()
    plot_topic_chart()