# todo/forms.py
from django import forms
from .models import Task

class JapaneseFileInput(forms.ClearableFileInput):
    initial_text = '現在の画像'
    input_text = '変更'
    clear_checkbox_label = '削除'

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'completed', 'image']
        labels = {
            'title': 'タイトル',
            'description': '説明',
            'completed': '完了',
            'image': '画像',
        }
        help_texts = {
            'title': 'タスクのタイトルを入力してください。',
            'description': 'タスクの詳細を記入してください。',
            'completed': 'このタスクが完了した場合はチェックを入れてください。',
        }
        widgets = {
            'image': JapaneseFileInput,
        }