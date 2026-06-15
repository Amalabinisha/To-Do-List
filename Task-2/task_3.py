import json
import os
from datetime import datetime

class Colors:
    GREEN = '\033[92m'
    RED = '\033[91m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    PURPLE = '\033[95m'
    BOLD = '\033[1m'
    END = '\033[0m'

class TodoManager:
    def __init__(self, filename='todo_list.json'):
        self.filename = filename
        self.tasks = self.load_tasks()
    
    def load_tasks(self):
        """Load tasks from JSON file"""
        if os.path.exists(self.filename):
            try:
                with open(self.filename, 'r') as f:
                    return json.load(f)
            except:
                return []
        return []
    
    def save_tasks(self):
        """Save tasks to JSON file"""
        with open(self.filename, 'w') as f:
            json.dump(self.tasks, f, indent=4)
    
    def add_task(self):
        """Requirement: Add tasks"""
        print(f"\n{Colors.BLUE}=== Add New Task ==={Colors.END}")
        title = input("Task title: ").strip()
        if not title:
            print(f"{Colors.RED}Task title cannot be empty!{Colors.END}")
            return
        
        description = input("Description (optional): ").strip()
        priority = input("Priority High/Medium/Low [Medium]: ").strip().capitalize()
        if priority not in ['High', 'Medium', 'Low']:
            priority = 'Medium'
        
        due_date = input("Due date YYYY-MM-DD (optional): ").strip()
        
        task = {
            'id': len(self.tasks) + 1,
            'title': title,
            'description': description,
            'priority': priority,
            'due_date': due_date,
            'status': 'Pending',
            'created': datetime.now().strftime("%Y-%m-%d %H:%M")
        }
        
        self.tasks.append(task)
        self.save_tasks()
        print(f"{Colors.GREEN}Task added! ID: {task['id']}{Colors.END}")
    
    def view_tasks(self):
        """Requirement: View tasks"""
        if not self.tasks:
            print(f"{Colors.YELLOW}No tasks found! Add some first.{Colors.END}")
            return
        
        print(f"\n{Colors.BOLD}=== Your To-Do List ==={Colors.END}")
        print(f"{'ID':<4} {'Status':<10} {'Priority':<8} {'Title':<25} {'Due Date'}{Colors.END}")
        print("-" * 70)
        
        for task in self.tasks:
            # Color code by status and priority
            if task['status'] == 'Done':
                status_color = Colors.GREEN
            else:
                status_color = Colors.YELLOW
            
            if task['priority'] == 'High':
                priority_color = Colors.RED
            elif task['priority'] == 'Medium':
                priority_color = Colors.YELLOW
            else:
                priority_color = Colors.BLUE
            
            print(f"{task['id']:<4} {status_color}{task['status']:<10}{Colors.END} {priority_color}{task['priority']:<8}{Colors.END} {task['title']:<25} {task['due_date']}")
        
        # Show stats
        total = len(self.tasks)
        done = len([t for t in self.tasks if t['status'] == 'Done'])
        pending = total - done
        print(f"\n{Colors.PURPLE}Total: {total} | Done: {done} | Pending: {pending}{Colors.END}")
    
    def delete_task(self):
        """Requirement: Delete tasks"""
        self.view_tasks()
        if not self.tasks:
            return
        
        try:
            task_id = int(input(f"\nEnter Task ID to delete: ").strip())
            task = next((t for t in self.tasks if t['id'] == task_id), None)
            
            if not task:
                print(f"{Colors.RED}Task ID not found!{Colors.END}")
                return
            
            confirm = input(f"Delete '{task['title']}'? (y/n): ").lower()
            if confirm == 'y':
                self.tasks = [t for t in self.tasks if t['id']!= task_id]
                # Re-number IDs to keep them sequential
                for i, task in enumerate(self.tasks, 1):
                    task['id'] = i
                self.save_tasks()
                print(f"{Colors.GREEN}Task deleted!{Colors.END}")
            else:
                print("Cancelled.")
                
        except ValueError:
            print(f"{Colors.RED}Please enter a valid number{Colors.END}")
    
    def mark_complete(self):
        """Extra: Mark task as done"""
        self.view_tasks()
        if not self.tasks:
            return
        
        try:
            task_id = int(input(f"\nEnter Task ID to mark complete: ").strip())
            task = next((t for t in self.tasks if t['id'] == task_id), None)
            
            if not task:
                print(f"{Colors.RED}Task ID not found!{Colors.END}")
                return
            
            if task['status'] == 'Done':
                print(f"{Colors.YELLOW}Task already completed!{Colors.END}")
                return
                
            task['status'] = 'Done'
            task['completed_date'] = datetime.now().strftime("%Y-%m-%d %H:%M")
            self.save_tasks()
            print(f"{Colors.GREEN}Task marked as complete!{Colors.END}")
            
        except ValueError:
            print(f"{Colors.RED}Please enter a valid number{Colors.END}")
    
    def filter_tasks(self):
        """Extra: Filter by status or priority"""
        print(f"\n{Colors.BOLD}Filter by:{Colors.END}")
        print("1. Status: Pending")
        print("2. Status: Done") 
        print("3. Priority: High")
        print("4. Priority: Medium")
        print("5. Priority: Low")
        
        choice = input("Select filter: ").strip()
        filtered = []
        
        if choice == '1':
            filtered = [t for t in self.tasks if t['status'] == 'Pending']
        elif choice == '2':
            filtered = [t for t in self.tasks if t['status'] == 'Done']
        elif choice == '3':
            filtered = [t for t in self.tasks if t['priority'] == 'High']
        elif choice == '4':
            filtered = [t for t in self.tasks if t['priority'] == 'Medium']
        elif choice == '5':
            filtered = [t for t in self.tasks if t['priority'] == 'Low']
        else:
            print(f"{Colors.RED}Invalid choice!{Colors.END}")
            return
        
        if not filtered:
            print(f"{Colors.YELLOW}No tasks match this filter{Colors.END}")
            return
            
        print(f"\n{Colors.BOLD}=== Filtered Tasks ==={Colors.END}")
        for task in filtered:
            print(f"ID {task['id']}: {task['title']} | {task['status']} | {task['priority']}")

def main():
    """Requirement: Menu-driven CLI program"""
    manager = TodoManager()
    
    while True:
        print(f"\n{Colors.BOLD}{Colors.PURPLE}=== To-Do List Manager ==={Colors.END}")
        print("1. Add Task")
        print("2. View All Tasks") 
        print("3. Mark Task Complete")
        print("4. Delete Task")
        print("5. Filter Tasks")
        print("6. Exit")
        
        choice = input(f"{Colors.BOLD}Enter choice (1-6): {Colors.END}").strip()
        
        if choice == '1':
            manager.add_task()
        elif choice == '2':
            manager.view_tasks()
        elif choice == '3':
            manager.mark_complete()
        elif choice == '4':
            manager.delete_task()
        elif choice == '5':
            manager.filter_tasks()
        elif choice == '6':
            print(f"{Colors.GREEN}All tasks saved. Goodbye!{Colors.END}")
            break
        else:
            print(f"{Colors.RED}Invalid choice! Pick 1-6{Colors.END}")

if __name__ == "__main__":
    main()